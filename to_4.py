import cv2
import time
import random


cap = cv2.VideoCapture(0)

face_dict = {}
face_dict[0] = 0, 0, 0, 0, 0, 0, 0
face_color = [0, 255, 3]
frame_stop = True
face_number = 0
face_max = 0
time_now = (time.time() % 10000)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    # print(face_color)
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    if face_max < len(faces):
        face_dict[face_max] = 0, 0, 0, 0, 0, 0, 0
        for i in range((len(faces)-face_max) * 3):
            face_color.append(random.randint(0, 255))

        face_max = len(faces)
    if frame_stop:
        for i in range(len(faces)):
            face_dict[i] = faces[i][0], faces[i][1], faces[i][2], faces[i][3], \
                           face_color[i*3], face_color[i*3+1], face_color[i*3+2]

    frame_stop = not frame_stop

    for i in range(len(faces)):
        if abs(face_dict[i][0]-faces[i][0]) < 20:
            cv2.rectangle(frame, (faces[i][0], faces[i][1]), (faces[i][0] + faces[i][2], faces[i][1] + faces[i][3]),
                          (face_dict[i][4], face_dict[i][5], face_dict[i][6], 2))
        else:
            print(1)
        if face_max < len(faces):
            face_max = len(faces)
            face_dict[face_max] = 0, 0, 0, 0, 0, 0, 0

    cv2.imshow("video", frame)
    # print(face_dict)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
