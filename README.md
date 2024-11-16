# Room Monitor System

### **Overview**
The Room Monitor System is an intelligent surveillance application that leverages computer vision and AI-based natural language processing to detect unauthorized room entries. Upon detecting a person in the monitored area, it generates an alert message using OpenAI's GPT-based API and sends an email notification to the owner.

This project combines state-of-the-art machine learning models, real-time video processing, and automated messaging to ensure effective room monitoring.

---

### **Features**
- **Real-Time Object Detection**: Uses a YOLO-based pre-trained model to identify people in the monitored area.
- **AI-Generated Alerts**: Employs OpenAI's GPT API to generate custom alert messages.
- **Email Notifications**: Automatically sends alerts via email using SMTP.
- **Modular and Extensible**: Allows for easy integration of additional sensors or triggers.

---

### **Technologies and Libraries**
The system uses the following technologies and libraries:
1. **Python Libraries**:
   - `time`: Manages delays and scheduling.
   - `smtplib`: Sends email notifications using SMTP.
   - `cv2` (OpenCV): Captures and processes video frames from the webcam.
   - `ultralytics`: Provides the YOLO (You Only Look Once) object detection framework.
   - `email.mime`: Constructs and formats email messages.

2. **AI and ML Models**:
   - **YOLOv10n**: Detects persons in the camera feed.
   - **OpenAI GPT-4 API**: Generates contextual alert messages.

---

### **System Design**
The system consists of the following components:

1. **Video Capture**:
   - The webcam feed is continuously monitored using OpenCV (`cv2.VideoCapture`).
   - Frames are analyzed in real-time to detect the presence of a person.

2. **Person Detection**:
   - A YOLOv10n model (`ultralytics.YOLO`) identifies whether a person is present in the frame.

3. **Alert Generation**:
   - OpenAI GPT API generates a natural language alert when unauthorized entry is detected.
   - A pre-configured system message ensures consistent responses.

4. **Email Notification**:
   - Alerts are formatted and sent via Gmail's SMTP server to the owner's email.

5. **Fail-Safe Mechanisms**:
   - System exits gracefully on interruptions and releases the webcam feed (`cap.release`).

---

### **How It Works**
1. **Startup Delay**: The system waits for 10 minutes (`time.sleep(600)`) to avoid detecting the initial user presence during activation.
2. **Frame Analysis**: Continuously processes webcam frames to detect persons using YOLO.
3. **Alert Workflow**:
   - If a person is detected:
     - GPT API generates an alert message.
     - An email with the alert message is sent to the configured recipient.
     - The system pauses for 2 minutes before resuming detection.
   - If no person is detected, it logs that the room is secure.
4. **Shutdown**: The system can be interrupted manually using `KeyboardInterrupt` (Ctrl+C), releasing all resources.

---

### **Setup Instructions**
1. **Dependencies**:
   Install the required libraries:
   ```bash
   pip install opencv-python ultralytics openai
   ```

2. **Configuration**:
   - Replace the placeholder `api_key` with your OpenAI API key.
   - Update `sender_email`, `receiver_email`, and `password` with your Gmail credentials.

3. **Running the System**:
   - Execute the main script:
     ```bash
     python room_monitor.py
     ```

4. **Stopping the System**:
   - Use `Ctrl+C` to stop the application gracefully.

---

### **Future Enhancements**
- **Data Encryption**: Secure sensitive data like API keys and email credentials.
- **Enhanced Triggers**: Implement IoT-based motion sensors for better detection triggers.
- **Video Storage**: Save video clips of detected activity and send them with email alerts.
- **Improved Notification Systems**: Add SMS or push notifications using services like Twilio or Firebase.

---

### **Disclaimer**
Ensure you have the necessary permissions to monitor the area. Do not use this system for unauthorized surveillance.