# VisionCount

## Intelligent Video Object Detection, Tracking & Counting System

VisionCount is a computer vision project designed to detect, track, count, and analyze objects in video.

The initial application focuses on traffic and vehicle counting using object detection, multi-object tracking, line-crossing detection, and directional analysis.

## Project Objective

The objective of VisionCount is to process a traffic video frame by frame and identify objects crossing a defined counting region.

The system will:

- Detect objects using YOLO
- Track objects across video frames
- Assign unique tracking IDs
- Detect line crossings
- Determine movement direction
- Count objects without duplicate counting
- Generate class-wise traffic analytics
- Visualize results through a Streamlit dashboard

## Core Pipeline

Video Input  
↓  
Object Detection  
↓  
Object Tracking  
↓  
Line-Crossing Detection  
↓  
Direction Detection  
↓  
Object Counting  
↓  
Analytics  
↓  
Dashboard

## Technology Stack

- Python
- OpenCV
- YOLO
- ByteTrack
- NumPy
- Pandas
- Plotly
- Streamlit
- Git & GitHub

## Project Status

🚧 Currently under development.

## Planned Features

- Traffic video input
- Object detection
- Multi-object tracking
- Unique object IDs
- Line-crossing detection
- Direction detection
- Class-wise counting
- Traffic analytics
- Processed video output
- Interactive Streamlit dashboard
- Basic evaluation

## Project Structure

```text
VisionCount/
├── app/
├── src/
├── configs/
├── data/
│   ├── input/
│   └── output/
├── models/
├── tests/
├── notebooks/
├── screenshots/
├── .gitignore
└── README.md


## License

MIT License