# An-Automated-COVID-19-SOPs-Monitoring-and-Management-System

## Overview
This project focused on developing an intelligent system designed to monitor and manage COVID-19 Standard Operating Procedures (SOPs) in public spaces. It leverages deep learning models, computer vision, and embedded systems to ensure compliance with safety protocols such as face mask detection, social distancing, contactless temperature sensing, and SpO2 monitoring.

## Project Structure

The repository contains the following files and folders:

### 1. **Circuit Schematics**
- **Contents:** Hardware block diagram, software block diagram, and hardware connection diagrams.
- **Purpose:** Provides detailed insights into the hardware architecture and connections.

### 2. **Source Code Files**
- **Python Files:**
  - `a.py`: Face mask detection
  - `q.py`: Social distancing detection
  - `ard.py`: Communication between Jetson Nano and Arduino Uno, audio generation
- **Arduino File:**
  - `arduino.cc`: Controls temperature and SpO2 sensing
- **Models & Data Files:**
  - `model.tflite`: Trained model for face mask detection (7000-image dataset)
  - `SSD_MobileNet.caffemodel` & `SSD_MobileNet_prototxt.txt`: Pre-trained MobileNet v2 model for people detection
  - `file.txt` & `file2.txt`: Intermediate result files for system operations
  - `class_labels.txt`: Class labels for MobileNet v2

### 3. **Component Datasheets**
- **Contents:** Datasheets for all hardware components used in the prototype.
- **Purpose:** Reference material for future hardware modifications or troubleshooting.

### 4. **FYP Reports**
- **FYP-II Final Report:** Comprehensive documentation covering problem analysis, solution development, algorithms, user guide, and results.
- **FYP Summary:** Concise summary of the project, including key results and case scenarios.

### 5. **Project Videos**
- **Video Files:**
  - `Introduction.mp4`: Overview of the project team, advisor, and client
  - `Problem.mp4`: Explanation of the problem statement
  - `Problem Solved.mp4`: Development process of the solution
  - `Explanation.mp4`: Algorithmic explanations
  - `Demonstration.mp4`: Prototype demonstration with various scenarios
  - `Internal Wiring.mp4`: Explanation of internal hardware connections
  - `Complete FYP.mp4`: Compilation of all the above videos

### 6. **Instructions Folder**
- **Setup Guide:** `instructions for prototype set-up.txt` - Step-by-step instructions for hardware assembly and connections
- **Code Execution:** `instructions for running the code files.txt` - OS installation (JetPack 4.6) and code execution guide
- **User Manual:** Maintenance guidelines, user instructions, and troubleshooting tips

### 7. **Poster**
- **Contents:** Key features, hardware diagrams, project milestones, and highlights

### 8. **Presentations**
- **Folders:**
  - `FYP-I`: 7 presentations from the first project phase
  - `FYP-II`: 7 presentations from the second project phase

## Key Features
- Face Mask Detection
- Social Distancing Monitoring
- Contactless Body Temperature Sensing
- SpO2 Measurement
- Automated Door Locking & Unlocking Mechanism
- Real-Time Audio Assistance

## Technologies Used
- **Deep Learning Models:** CNN with Linear Regression, MobileNetv2
- **Libraries & Frameworks:** MediaPipe, OpenCV, TensorFlow, Keras
- **Hardware:**
  - Microprocessor: Nvidia Jetson Nano
  - Microcontroller: Arduino Uno
  - Sensors: MLX90614 (temperature), MAX30102 (SpO2), Sonar Sensor

## Getting Started
1. **Hardware Setup:** Refer to `instructions for prototype set-up.txt`
2. **Software Installation:** Follow `instructions for running the code files.txt`
3. **Run the System:** Execute `a.py` and `q.py` for monitoring, and `ard.py` for communication and control

## License
This project is developed as part of the Final Year Project at the National University of Computer & Emerging Sciences (FAST-NUCES), Lahore, Pakistan.

## Acknowledgments
- **Institution:** FAST-NUCES, Lahore, Pakistan
- **Team Members:** Maaheen Yasin (Team Lead), Ahmad Tameem, Inbisat Mudassar Dar 
- **Advisor & Co-Advisor:** Dr. Omer Saleem, Mr. Hamza Yousuf 
- **Industrial Client:** Saleem Steel Industries 

---

