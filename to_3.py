import numpy as np
import cv2
import time
import random


cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

face_dict = {}
# face_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
face_color = [0, 255, 3, 123, 60, 35, 78, 37]
frame_stop = True

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

    if frame_stop:
        for i in range(len(faces)):
            face_dict[i] = faces[i][0], faces[i][1], faces[i][2], faces[i][3], face_color[i*3], face_color[i*3+1], \
                           face_color[i*3+2]

    frame_stop = not frame_stop

    for i in range(len(faces)):
        if faces[i][0] - 50 < face_dict[i][0] < faces[i][0] + 50:
            cv2.rectangle(frame, (faces[i][0], faces[i][1]), (faces[i][0] + faces[i][2], faces[i][1] + faces[i][3]),
                          (face_color[i*3], face_color[i*3+1], face_color[i*3+2], 2))
            print(1)
        else:
            print(2)
            # face_dict[i] = faces[i][0], faces[i][1], faces[i][2], faces[i][3], 0, 255, 0

        print(face_dict)

    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
