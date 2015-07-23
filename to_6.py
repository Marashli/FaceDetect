import cv2
import time
import random


cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces_data = []
time_now = (time.time() % 10000)
faces_max = 0

while True:
    ret, frame = cap.read()

    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    # print(faces_max)
    # добавление при необходимости новый элемент в массив
    if len(faces) > faces_max:
        faces_data.append([0, 0, 0, 0, 0])
        faces_max += 1
    # работ]

    if len(faces) < 1:
        if (time.time() % 10000) - time_now > 1:
            pass
            # print('Ты продержался всго лишь', int((time.time() % 10000) - time_now), 'секунд')
        time_now = (time.time() % 10000)

    for i in range(len(faces)):
        # faces_data[i] = list(faces[i])
        for j in range(4):
            faces_data[i][j] = faces[i][j]

    # print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255, 2))
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(faces_data)

cap.release()
cv2.destroyAllWindows()