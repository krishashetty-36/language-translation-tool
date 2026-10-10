# Object Detection and Tracking

## Project Overview

Object Detection and Tracking is a computer vision project developed using Python, OpenCV, and the YOLO object detection model. It detects objects in video frames and tracks their movement by assigning tracking IDs where available.

The project supports both live webcam input and recorded video files.

## Features

- Real-time object detection using a webcam
- Object detection from recorded videos
- Object tracking with tracking IDs
- Bounding boxes around detected objects
- Saves processed video output
- Simple menu-based interface

## Technologies Used

- Python 3.12
- OpenCV
- Ultralytics YOLO11n
- ByteTrack tracker

## Project Structure

```text
CodeAlpha-Task-4-Object-Detection-Tracking/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── videos/
├── output/
├── venv/
├── venv312/
└── yolo11n.pt
```

**Note:** The virtual environments, downloaded model weights, and generated output files are excluded from GitHub using `.gitignore`.

## Installation

### Prerequisites

- Python 3.12
- Visual Studio Code
- A webcam for live detection, or a recorded video for video processing

### Setup Instructions

1. Clone or download the project repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project directory.
4. Create a virtual environment:

   ```powershell
   python -m venv venv312
   ```

5. Install the dependencies:

   ```powershell
   .\venv312\Scripts\python.exe -m pip install -r requirements.txt
   ```

## How to Run

Run the following command in the VS Code terminal:

```powershell
.\venv312\Scripts\python.exe main.py
```

The application displays a menu with two options.

### Option 1: Webcam

Enter `1` to start real-time object detection and tracking using your webcam.

### Option 2: Recorded Video

1. Place your video file inside the `videos` folder.
2. Enter `2` in the application menu.
3. Enter the video filename, including its extension, when prompted.

The application processes the video and displays the detected objects and tracking IDs.

Press `Q` while the video window is active to stop processing.

## Output

The processed video is saved at:

`output/tracked_output.mp4`

The output includes bounding boxes, object labels, and tracking IDs where available.

## Applications

- Traffic monitoring
- People and vehicle tracking
- Video surveillance prototypes
- Movement analysis
- Computer vision learning and experimentation

## Future Enhancements

- Add object counting
- Display detection statistics
- Support additional video formats
- Improve performance for real-time applications

## Conclusion

This project demonstrates how object detection and object tracking can be combined to analyze

