# Video-To-mp3-converter
This is a simple Python GUI application that allows users to convert local video files (such as .mp4, .avi, .mov, etc.) to MP3 audio files. The user can select a video file from their computer using a file dialog, and the app will extract the audio and save it as an MP3 file in the same folder as the video.

Features:
Convert any local video file to MP3 format.
Simple and user-friendly graphical interface built with tkinter.
Automatically saves the MP3 file in the same directory where the original video file is located.
Supports various video formats such as .mp4, .avi, .mov, and .mkv.

Prerequisites
Make sure you have Python 3.x installed and the following libraries:

Install moviepy for video processing and conversion:
pip install moviepy
Install tkinter (it is usually included with Python, but if not):

sudo apt-get install python3-tk  # For Linux
On Windows, tkinter comes pre-installed with Python.

How to Use : 
Clone or download the repository to your local machine.
Open a terminal or command prompt in the project directory.

Run the Python script:
python video_to_mp3_converter.py
A GUI window will open:
Click "Upload Video" to select a video file from your computer.
After selecting the video file, click "Convert to MP3."
The application will extract the audio from the video and save it as an MP3 file in the same directory as the video.

Project Structure
video_to_mp3_converter/
│
├── video_to_mp3_converter.py  # Main Python script
├── README.md                  # This file
└── requirements.txt           # List of dependencies (optional)

Example
Click "Upload Video" to browse and select a video file like example_video.mp4.
Click "Convert to MP3."
After the conversion is complete, the MP3 file will be saved in the same folder as example_video.mp4, with the same base name (e.g., example_video.mp3).
Troubleshooting
Unsupported Video Format: Ensure that the video file you are trying to convert is a supported format such as .mp4, .avi, .mov, or .mkv.
Permission Errors: If you encounter permission issues while saving the MP3 file, try running the script as an administrator.
No Video Selected: Ensure you have uploaded a video file before clicking "Convert to MP3."

License
This project is licensed under the MIT License - see the LICENSE file for details.
