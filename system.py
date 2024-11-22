# import libs
import os
import time
import smtplib
import cv2, sys
import numpy as np
from PIL import Image
from openai import OpenAI
from ultralytics import YOLO
from datetime import datetime
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Load environment variables from a .env file
load_dotenv()

#/* section 1: ...*/
api_key = os.getenv('API_KEY')
client = OpenAI(api_key = api_key)

#/* section 2: ...*/
person = 0
cap = cv2.VideoCapture(1) 
model = YOLO("yolo11n.pt")

#/* section 3: ...*/
model_gpt="gpt-4o-mini"
max_completion_tokens=150
prompt = "strange person detected!"
sys_msg = "You are a helpful assistant, you are monitoring my room, evertime somebody enters you write an alert email, my name is Joh Doe"

#/* section 4: ...*/
sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')
start_keyword = "Dear"
password = os.getenv('PASSWORD')

def get_answer(prompt) -> str:
    try:
        completion = client.chat.completions.create(
            model=model_gpt,
            max_completion_tokens=max_completion_tokens,
            messages=[
                {"role": "system", "content": sys_msg},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error debug: {e}")

def check_person(frame) -> bool:
    try:
        results = model(source=frame, verbose=False)
        for result in results:
            for aux in result.boxes:
                if (int(aux.cls[0])) == person:
                    print("person detected")
                    return True
    except Exception as e:
        print(f"Error :{e}")
    return False

def send_message(alert, file) -> None:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Unauthorized Presence Detected"
    body = alert
    msg.attach(MIMEText(body, 'plain'))

    with open(file, "rb") as f:
        img = MIMEImage(f.read(), _subtype="png")
        msg.attach(img)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

def get_intruder()-> str:
    filename = datetime.now().strftime("%Y-%m-%dH%H-%M-%S.png")
    try:
        _, frame = cap.read()
        data = frame.astype(np.uint8)
        image = Image.fromarray(data) 
        image.save(filename)
        return filename
    except Exception as e:
        print(f"Error: {e}")

def clean_up() -> None:
    cap.release()
    sys.exit() 

if __name__ == "__main__":
    print("System Awake")
    time.sleep(180) #10min
    while True:
        try:
            _, frame = cap.read()
            if check_person(frame):
                filename = get_intruder()
                answer = get_answer(prompt)
                if answer:
                    answer = answer[answer.index(start_keyword):]
                    send_message(answer, filename)
                    time.sleep(120) #2min
        except KeyboardInterrupt:
            clean_up()