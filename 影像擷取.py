import cv2
import os
import ssl
import time
from urllib.request import urlretrieve


def download_media(url, save_dir, media_type):
    # Get current time as a string in the format YYYY-MM-DD_HHmm
    time_str = time.strftime("%Y-%m-%d_%Hh%M", time.localtime())
    # Allow unverified SSL certificates
    ssl._create_default_https_context = ssl._create_unverified_context

    if media_type == 'video':
        # Capture a frame from the video at the given URL
        vidcap = cv2.VideoCapture(url)
        success, image = vidcap.read()
        vidcap.release()
    elif media_type == 'image':
        # Download an image from the given URL
        image, _ = urlretrieve(url)

    # Save the image to a file with the current time in its name
    save_path = os.path.join(save_dir, f'{time_str}.png')
    cv2.imwrite(save_path, image)

    
def capture_media(media_type, url, camera_name):
    # Create a directory to store the captured media, if it doesn't already exist
    save_dir = f'./{camera_name}/'
    os.makedirs(save_dir, exist_ok=True)
    
    while True:
        try:
            # Download or capture a frame from the media at the given URL
            download_media(url, save_dir, media_type)
        except Exception as e:
            print(f'An Error occurred: {e}')
        # Wait until the next minute starts
        time.sleep(60 - time.time() % 60)


if __name__ == '__main__':
    # Get user input for media type, URL, and camera name
    media_type = input('Enter media type to capture (image/video): ')
    url = input('Enter URL to capture from: ')
    camera_name = input('Enter name of camera location: ')
    
    # Start capturing media at the given URL
    capture_media(media_type, url, camera_name)