# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:20:12 2023

@author: USER
"""
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,320) # set Width
cap.set(4,240) # set Height
while(True):
    ret, frame = cap.read()
    # frame = cv2.flip(frame, 1) # Flip camera
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        print("bye...")
        break
cap.release()
cv2.destroyAllWindows()