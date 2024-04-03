**Behavior Monitoring System**

**Overview**
The Behavior Monitoring System is an AI-powered application designed to analyze student behavior in real-time during lectures. It utilizes facial expression analysis to evaluate students' engagement and generates reports to showcase their class involvement.

**Motivation**
The aim of this project is to provide educators with a tool to assess student engagement and participation during lectures. By leveraging artificial intelligence and computer vision techniques, the system can provide valuable insights into students' behaviors, allowing educators to adapt their teaching methods accordingly.

**Features**
- Real-time Facial Expression Analysis: The system analyzes students' facial expressions in real-time to assess their level of engagement.
- User-Friendly Interface: The application features a user-friendly interface for easy interaction and navigation.
- Customizable Settings: Users can customize settings to suit different classroom environments and teaching styles.
- Automatic Report Generation: The system automatically generates engagement reports, providing educators with valuable insights into student behavior.

**Implementation**
**Project Structure**

- ui/
  - __init__.py: Initializes the UI package.
  - app_ui.py: Contains the main window and layout setup.
  - components.py: Defines GUI components such as buttons and labels.
  
- video_processing/
  - __init__.py: Initializes the video processing package.
  - capture.py: Manages video capture from webcam.
  - face_detection.py: Detects faces in video frames.
  
- analysis/
  - __init__.py: Initializes the analysis package.
  - emotion_recognition.py: Analyzes facial expressions for emotion recognition.
  
- reporting/
  - __init__.py: Initializes the reporting package.
  - report_generator.py: Generates engagement reports.
  - data_store.py: Manages data storage and retrieval for reports.
  
- utils/
  - __init__.py: Initializes the utils package.
  - config_loader.py: Loads application configuration settings.
  - logger.py: Implements application-wide logging functionality.
  
- models/
  - __init__.py: Initializes the models package.

**Technologies Used**
- Python: Core programming language.
- OpenCV: Video processing and face detection.
- Tkinter: GUI development.
- Pillow: Image processing library.
- Other Dependencies: Listed in the requirements.txt file.

**Getting Started**
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the `main.py` file to launch the application.

**Usage**
1. Launch the application.
2. Select the desired classroom.
3. Begin the lecture.
4. The application will analyze students' behavior in real-time and generate engagement reports.

**Requirements**
The following dependencies are required to run the application:
- opencv-python==4.5.4
- numpy==1.21.2
- Pillow==8.4.0

**Contributors**
Veetrag Nahar: Project Lead

**Confidentiality Notice**
Due to business conflict, I am unable to upload the entire project code here. However, feel free to reach out to me via email at veetragnahr@gmail.com for a demo and potential collaboration opportunities.
