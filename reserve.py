import numpy as np
import cv2
import time
import random


cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

face_dict = {}
face_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
faceCascade = cv2.CascadeClassifier(cascPath)

time_now = (time.time() % 10000)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    if len(faces) < 1:
        if (time.time() % 10000) - time_now > 1:
            print('Ты продержался всго лишь', int((time.time() % 10000) - time_now), 'секунд')
        time_now = (time.time() % 10000)
    # print("Found {0} faces!".format(len(faces)))
    for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255, 2))
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
