import numpy as np
import cv2
import time
import random


cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

face_dict = {}
face_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
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
    # if len(faces) < 1:
    #    if (time.time() % 10000) - time_now > 1:
    #        print('Ты продержался всго лишь', int((time.time() % 10000) - time_now), 'секунд')
    #    time_now = (time.time() % 10000)
    # print("Found {0} faces!".format(len(faces)))

    if frame_stop:
        for i in range(len(faces)):
            face_dict[i] = faces[i][0], faces[i][1], faces[i][2], faces[i][3], 0, 255, 0

    if faces[0][0] - 50 < face_dict[0][0] < faces[0][0] + 50:
        cv2.rectangle(frame, (faces[0][0], faces[0][1]), (faces[0][0] + faces[0][2], faces[0][1] + faces[0][3]), (0, 0, 0, 2))
        # print(1)
    else:
        pass
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0, 2))
        # print(2)

    frame_stop = not frame_stop
    # for (x, y, w, h) in faces:
    #   cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0, 2))
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(face_dict)
cap.release()
cv2.destroyAllWindows()
