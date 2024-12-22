# Advanced Driver Safety System

## Introduction
The Advanced Driver Safety System is a comprehensive project aimed at improving road safety by detecting driver drowsiness and performing real-time object detection on the road. The system uses advanced sensors and algorithms to monitor the driver’s state and send continuous emergency notifications if sleep is detected. This proactive approach is designed to prevent accidents caused by drowsy driving.

This repository contains the source code, which integrates computer vision techniques with machine learning algorithms to combat the dangers of drowsy driving.

## Capabilities
    1. Drowsiness Monitoring: Utilizes facial landmark detection to track the driver's eye blinking patterns, assessing their level of alertness.
    
    2. Real-Time Notification: This feature now includes continuous notifications to alert the driver if they fall asleep. Upon detecting sleep, the system triggers notifications with gentle vibrations on a smartwatch and escalating audio alerts on a phone, providing a multi-sensory wake-up cue to increase the likelihood of rousing the driver.

    3. Object Recognition: Uses the YOLO (You Only Look Once) v8 model to identify objects on the road, such as vehicles (Cars, Buses, Trucks, Motorcycles, and Bicycles) and pedestrians, delivering real-time hazard analysis.

## Idea
    1. The sleep detection system uses a combination of camera feeds and physiological signals to monitor the driver’s alertness.
    2. If signs of sleep are detected, an emergency notification is sent to the driver through auditory (e.g., loud alarm) and visual (e.g., flashing lights) signals.
    3. The object detection system continuously scans the road for potential hazards, providing real-time alerts to the driver to take corrective actions.

## Key Notification Features
    1. Smartwatch Vibration Notification: Upon detecting sleep, the smartwatch will emit gentle vibrations.
    2. Phone Audio Alert: Concurrently, the phone will start an escalating audio alert to complement the vibration cues.
    3. Multi-Sensory Wake-Up Cue: By combining vibrations and audio alerts, the system enhances the chances of waking the user effectively.

## Installation
1. Prerequisites: Ensure Python is installed along with the required libraries listed in requirements.txt.

2. Clone Repository: Clone this repository to your local machine.

3. Download Models: Obtain the pre-trained YOLO model (yolov8n.pt) and the facial landmark detection model (shape_predictor_68_face_landmarks.dat), and place them in the specified directories.

4. Install Dependencies: Run the following command to install the necessary Python libraries:

    ```pip install -r requirements.txt```


5. Launch the System: Execute the main.py script to start the Advanced Driver Safety System.

6. Configuration: Modify the dash.py file to set different detection parameters as needed.

## How to Use

- Run the main.py script with appropriate video inputs for the dashcam and front-facing camera.
- Observe the output windows for real-time drowsiness monitoring and object detection results.
- Real-time notification will be sent to phone and watch.

## Implementation Details For Notification
    - Notification Trigger: The notification system is triggered immediately upon sleep detection.
    - Vibration Pattern: The smartwatch vibration is set to a gentle pattern to avoid startling the user but sufficient to be felt.
    - Audio Alert Escalation: The audio alert on the phone starts at a low volume and gradually increases to ensure it captures the user’s attention without causing abrupt disturbance.
    - User Experience: The multi-sensory approach is designed to be subtle yet effective, ensuring a balanced and pleasant wake-up experience.

# Credits
- This project utilizes the YOLO object detection model and the dlib library for facial landmark detection.
- A special thanks to **Sulav Kumar Shrestha**, for laying the groundwork for the Advanced Driver Safety System.


<img width="2207" alt="notification" src="https://github.com/RATHOD-SHUBHAM/DriverAssistant/assets/58945964/c97a669e-3a39-4e8a-95c2-e7357737b6b8">


![IMG_9641](https://github.com/RATHOD-SHUBHAM/DriverAssistant/assets/58945964/c5e456f7-5bfd-49b6-9f8c-194db6a60fb9)
