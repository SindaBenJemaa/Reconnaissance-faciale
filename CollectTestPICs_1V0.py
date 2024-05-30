import cv2

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
id = 1
Num = 0

while True:
    ret, img = cam.read()
    # img = cv2.flip(img, 0)
    face = facedetect.detectMultiScale(img, 1.3, 5)

    for (x,y,w,h) in face:
        Num += 1
        #sauvegarder les photos dans le dossier dataset
        if cv2.waitKey(100) & 0xff == ord(' '):
            cv2.imwrite("dataset/User." + str(id) + '.' + str(Num) + ".jpg", img[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow("reconnaissance faciale", img)

        if cv2.waitKey(100) & 0xff == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()    

