import numpy as np
import cv2
import time
import random


cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

face_time = [0, 0]
faceCascade = cv2.CascadeClassifier(cascPath)

time_now_1 = (time.time() % 10000)
time_now_2 = (time.time() % 10000)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
            if x < 150:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255, 2))
                face_time[0] = int((time.time() % 10000)) - int(time_now_1)
                time_now_1 = time.time() % 10000
            elif x > 250:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0, 2))
                face_time[1] = int((time.time() % 10000)) - int(time_now_2)
                time_now_2 = time.time() % 10000

    cv2.imshow("video", frame)
    print(face_time)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
