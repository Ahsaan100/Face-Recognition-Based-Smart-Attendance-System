import cv2
import pickle
import numpy as np
import os

video = cv2.VideoCapture(0) #for internal webcam we use 0
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i = 0

name = input("Enter Your Name: ")
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting the image to Grayscale because Casscade Classifier works best with grayscale images
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces: # x and y are coordinates while w and h are width and height
        crop_img = frame[y: y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50,50))
        if len(faces_data)<=100 and i%10==0:
            faces_data.append(resized_img) #storing the faces data in the list
        i = i+1  
        cv2.putText(frame , str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1) #rectangle for bounding box

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k== ord('q') or len(faces_data)==100:
        break
video.release
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data)  #converting the data into numpy array
faces_data = faces_data.reshape(100, -1)

if "names.pkl" not in os.listdir('data/'): #checks if the file is not present in data folder, it will create the name.pkl file
    names = [name]*100
    with open('data/names.pkl','wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names+[name]*100
    with open('data/names.pkl', 'wb') as f:
            pickle.dump(names, f)

if "faces_data.pkl" not in os.listdir('data/'): #checks if the file is not present in data folder, it will create the name.pkl file
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis = 0)
    with open('data/faces_data.pkl', 'wb') as f:
            pickle.dump(faces, f)