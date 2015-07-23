import numpy as np
import cv2
import time
import random


cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

face_dict = {}
face_numb = 0
face_color = []
# face_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
faceCascade = cv2.CascadeClassifier(cascPath)

time_now = (time.time() % 10000)
q = 0

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
        # создание цветов
        if face_numb < len(faces):
            for i in range(3):
                face_color.append(random.randint(0, 255))
            face_numb += 1
        wait = 0
        if q % 2 == 0:
            face_dict[len(faces)] = x, y, w, h, face_color[3*(len(faces)-1)+0], face_color[3*(len(faces)-1)+1], face_color[3*(len(faces)-1)+2]
            wait = 1
        q += 1


        if (face_dict[1][0] - 20 < faces[0][0] < face_dict[1][0] + 20) and (face_dict[1][1] - 20 < faces[0][1] < face_dict[1][1] + 20):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (face_color[3*(len(faces)-1)+0], face_color[3*(len(faces)-1)+1], face_color[3*(len(faces)-1)+2], 2))
            #print('1')
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0, 2))
        # face_str = str(x) + str(y) + str(w) + str(h)
        # print(face_str)
        # print(face_dict[1][0], faces[0][0])
        # print(face_dict[1][1], faces[0][1])
        #print(face_dict[1][0], faces[0][0])
        #print(face_dict)
        if len(faces) > 1 and wait == 0:
            print('------------------------------------')
            print('первый человек - сравннение по x', faces[0][0], face_dict[1][0])
            print('первый человек - сравннение по y', faces[0][1], face_dict[1][1])
            print('первый человек - сравннение по x', faces[1][0], face_dict[2][0])
            print('первый человек - сравннение по y', faces[0][1], face_dict[2][1])
            print(face_dict[2])
        wait = 0
        print(face_dict)


        #print(face_dict[1][0])





    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
