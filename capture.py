import cv2
import os
import ssl
import time
import requests
import numpy as np
from typing import Union


def download_media(url: str, save_dir: str, media_type: str) -> None:
    """
    Downloads an image or a frame from a video at a given URL and saves it.

    Args:
        url (str): The URL of the image or video to download.
        save_dir (str): The directory to save the downloaded image or frame.
        media_type (str): The type of media to download ('image' or 'video').

    Raises:
        ValueError: If `media_type` is not 'image' or 'video'.
    """
    # Get current time as a string in the format YYYY-MM-DD_HHmm
    time_str = time.strftime("%Y-%m-%d_%Hh%M", time.localtime())
    # Allow unverified SSL certificates
    ssl._create_default_https_context = ssl._create_unverified_context

    if media_type == 'video':
        # Capture a frame from the video at the given URL
        vidcap = cv2.VideoCapture(url)
        success, image = vidcap.read()
        if not success:
            raise ValueError(f"Failed to read video at {url}")
        vidcap.release()
    elif media_type == 'image':
        # Download an image from the given URL using requests
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response
        image_data = np.frombuffer(response.content, dtype=np.uint8)
        image = cv2.imdecode(image_data, cv2.IMREAD_UNCHANGED)
    else:
        raise ValueError("'media_type' must be either 'image' or 'video'")

    # Save the image to a file with the current time in its name
    save_path = os.path.join(save_dir, f'{time_str}.png')
    cv2.imwrite(save_path, image)


def capture_media(media_type: str, url: str, camera_name: str) -> None:
    """
    Continuously captures media from a given URL and saves it.

    Args:
        media_type (str): The type of media to capture ('image' or 'video').
        url (str): The URL to capture from.
        camera_name (str): The name of the camera location.
    """
    # Create a directory to store the captured media, if it doesn't already exist
    save_dir = f'./{camera_name}/'
    os.makedirs(save_dir, exist_ok=True)
    
    while True:
        try:
            # Download or capture a frame from the media at the given URL
            download_media(url, save_dir, media_type)
        except Exception as e:
            print(f'An error occurred: {e}')
        # Wait until the next minute starts
        time.sleep(60 - time.time() % 60)


if __name__ == '__main__':
    # Get user input for media type, URL, and camera name
    media_type = input('Enter media type to capture (image/video): ')
    url = input('Enter URL to capture from: ')
    camera_name = input('Enter name of camera location: ')
    
    # Start capturing media at the given URL
    capture_media(media_type, url, camera_name)
