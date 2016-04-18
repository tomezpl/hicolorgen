# hicolorgen
## Description
Free Ubuntu hicolor icon generator, written in Python with OpenCV libraries.

## Installing and set-up
### Python
The script seems to work fine with Python 2.7.6.
You can run this command to install it, although it should come with a standard Ubuntu 14.04 installation:
    sudo apt-get install python2.7

### Dependencies
Since the script is written with OpenCV, you will need to install that. This apt command should install all necessary libraries and bindings for Python:
    sudo apt-get install python-opencv

## Usage
This is the command format used by the script:
    python generate.py <path-to-source-icon-image-file>
You may have to execute this with root privileges, which will result in
    sudo python generate.py <path-to-source-icon-image-file>
If your source icon image file path contains spaces, be sure to put the path in quotes.