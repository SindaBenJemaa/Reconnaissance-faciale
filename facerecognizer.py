# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:55:46 2023

@author: USER
"""

import cv2, imutils, face_recognition, imutils, pickle, time
from imutils.video import VideoStream
from imutils.video import FPS
screensize=600
tagSize=.4
green=(0,255,0)
defaultName="X"
encodingsP="encodings.pickle"
cascade="haarcascade_frontalface_default.xml"
print("loading data, pls wait...")
data = pickle.loads(open(encodingsP, "rb").read())
detector = cv2.CascadeClassifier(cascade)
print("starting video stream")
cam=cv2.VideoCapture(0)
time.sleep(1.0)
while True:
    ret,frame=cam.read()
    frame=imutils.resize(frame, width=screensize)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # for face detection
    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # for face recognition
    rects=detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    boxes=[(y,x + w,y+h,x) for (x,y,w,h) in rects]
    encodings=face_recognition.face_encodings(rgb,boxes)
    names=[]
    for encoding in encodings:
        matches=face_recognition.compare_faces(data["encodings"],encoding)
        name="Unknown"
        if True in matches:
            matchedIdxs=[i for (i,b) in enumerate(matches) if b]
            counts={}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
            if defaultName != name:
                defaultName = name
                print("Hello",defaultName)
        names.append(name)
    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame,(left,top),(right,bottom),green,1)
        y=top-5 if top-5>5 else top+5
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,tagSize, green,1)
    cv2.imshow("FaceRecognizer ('q' to quit)", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        print("bye...")
        break
cv2.destroyAllWindows()
cam.stop()
