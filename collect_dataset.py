# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:52:22 2023

@author: USER
"""

import cv2

name = 'dataset'

cam = cv2.VideoCapture(0)
cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)
img_counter = 0
print("press ’q’ to quit")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)
    k = cv2.waitKey(1)
    if k%256 == ord("q"):
        print("bye...")
        break
    elif k%256 == 32:  # "space"
        img_name = "F:\Projet-reconnaissance\tp4\dataset"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} stored".format(img_name))
        img_counter += 1
cam.release()
cv2.destroyAllWindows()

