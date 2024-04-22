from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime

from win32com.client import Dispatch

def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

video = cv2.VideoCapture(0) #for internal webcam we use 0
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

img_background = cv2.imread('data/background.png')

COL_NAMES = ['NAME', 'TIME']

with open('data/names.pkl', 'rb') as w:
        LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting the image to Grayscale because Casscade Classifier works best with grayscale images
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces: # x and y are coordinates while w and h are width and height
        crop_img = frame[y: y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50,50)).flatten().reshape(1,-1)
        output = knn.predict(resized_img)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y") #creating date
        timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S") #creating timestamp
        exist=os.path.isfile("Attendance/Attendance_" + date + ".csv") 
        # for a viually better bounding box, use the following 3 lines of code
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 2)
        cv2.rectangle(frame, (x,y-40), (x+w, y), (50,50,255), -1)
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1) #rectangle for bounding box
        attendance=[str(output[0]), str(timestamp)]
    img_background[162:162 + 480, 55:55 + 640] = frame    
    cv2.imshow("Frame",img_background)
    k = cv2.waitKey(1)
    if k== ord('q'):
        break
    if k==ord('o'):
        speak("Attendance Taken..")
        time.sleep(3)
        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
            csvfile.close()
video.release()
cv2.destroyAllWindows()
