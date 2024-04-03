Behavior Monitoring System
Overview
The Behavior Monitoring System is an AI-powered application designed to analyze student behavior in real-time during lectures. It utilizes facial expression analysis to evaluate students' engagement and generates reports to showcase their class involvement.

Motivation
The aim of this project is to provide educators with a tool to assess student engagement and participation during lectures. By leveraging artificial intelligence and computer vision techniques, the system can provide valuable insights into students' behaviors, allowing educators to adapt their teaching methods accordingly.

Features
Real-time Facial Expression Analysis: The system analyzes students' facial expressions in real-time to assess their level of engagement.
User-Friendly Interface: The application features a user-friendly interface for easy interaction and navigation.
Customizable Settings: Users can customize settings to suit different classroom environments and teaching styles.
Automatic Report Generation: The system automatically generates engagement reports, providing educators with valuable insights into student behavior.
Implementation
Project Structure
The project is structured into several modules:

ui/
Contains the user interface components and logic.

__init__.py: Initializes the UI package.
app_ui.py: Contains the main window and layout setup.
components.py: Defines GUI components such as buttons and labels.
video_processing/
Handles video capture and face detection.

__init__.py: Initializes the video processing package.
capture.py: Manages video capture from webcam.
face_detection.py: Detects faces in video frames.
analysis/
Performs facial expression analysis.

__init__.py: Initializes the analysis package.
emotion_recognition.py: Analyzes facial expressions for emotion recognition.
reporting/
Generates engagement reports.

__init__.py: Initializes the reporting package.
report_generator.py: Generates engagement reports.
data_store.py: Manages data storage and retrieval for reports.
utils/
Provides utility functions.

__init__.py: Initializes the utils package.
config_loader.py: Loads application configuration settings.
logger.py: Implements application-wide logging functionality.
models/
(Optional) Contains custom models or information about using open-source models.

Technologies Used
Python: Core programming language.
OpenCV: Video processing and face detection.
Tkinter: GUI development.
Pillow: Image processing library.
Other Dependencies: Listed in the requirements.txt file.
Getting Started
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the main.py file to launch the application.
Usage
Launch the application.
Select the desired classroom.
Begin the lecture.
The application will analyze students' behavior in real-time and generate engagement reports.
Requirements
The following dependencies are required to run the application:
opencv-python==4.5.4
numpy==1.21.2
Pillow==8.4.0

Contributors
Veetrag Nahar: Project Lead

Confidentiality Notice
Due to business conflict, I am unable to upload the entire project code here. However, feel free to reach out to me via email at veetragnahr@gmail.com for a demo and potential collaboration opportunities.