# Continuous Media Capture

This repository contains code for capturing continuous media (images or video frames) from a given URL, and saving the media frames to a local directory on disk. The media capture is performed at regular intervals of one minute, and the filename of each captured media frame includes a timestamp in the format YYYY-MM-DD_HHmm.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

To run the code, you need to have the following packages installed:

* Python 3
* OpenCV
* SSL
* urllib

## Getting Started

To use the code, you'll need to have Python 3 installed on your system. Clone this repository to your local machine and navigate to the root directory. Then, install the required dependencies using pip:

    pip install -r requirements.txt

## Usage

To capture continuous media, run the following command:

    python capture.py

You will be prompted to specify the media type (1 for video, 2 for image), the URL to capture from, and a name for the camera location. The captured media frames will be saved to a subdirectory with the camera name, which will be created if it does not already exist.

## Notes
If you want to stop the media capture, you can terminate the program by pressing Ctrl-C in the terminal.
The code is set to capture media frames at one-minute intervals, but this can be adjusted by changing the **time.sleep** value in the **download_media** functions.
The captured media frames are saved in the PNG format by default, but this can be changed by modifying the **cv2.imwrite** or **urlretrieve** functions, respectively.

## Contributing
If you find a bug or have an idea for a feature, please open an issue on this repository. Pull requests are also welcome.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
