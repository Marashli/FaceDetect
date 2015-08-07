import cv2
import time
import random

config = open('config.txt', 'r')
config = config.read()
config = config.split()
# print(config)


class Detect:
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    faces_data = []
    time_now = (time.time() % 10000)
    faces_max = 0

    for i in range(len(config) // 5):
        faces_data.append([int(config[5 * i + 0]), int(config[5 * i + 1]), int(config[5 * i + 2]) - int(config[5 * i + 0]),
                           int(config[5 * i + 3]) - int(config[5 * i + 1]), False,
                           random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 0,
                           int((time.time() % 10000))])

    # print(faces_data)
    while True:
        count = 0
        ret, frame = cap.read()

        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        # print(faces_max)

        if len(faces) > faces_max:
            while faces_max < len(faces):
                faces_data.append([0, 0, 0, 0, False, random.randint(0, 255), random.randint(0, 255),
                                   random.randint(0, 255), 0, int((time.time() % 10000))])
                faces_max += 1

        # print(faces_data)

        for i in range(len(faces)):
            if (abs(int(faces_data[i][0]) - int(faces[i][0]))) < 100 \
                    and (abs(int(faces_data[i][1]) - int(faces[i][1]))) < 100:

                cv2.rectangle(frame,
                              (faces[i][0], faces[i][1]),
                              (faces[i][0]+faces[i][2], faces[i][1]+faces[i][3]),
                              (faces_data[i][-5], faces_data[i][-4], faces_data[i][-3], 2))

                faces_data[i][-2] += int((time.time() % 10000)) - faces_data[i][-1]
                faces_data[i][-1] = int((time.time() % 10000))
            else:
                cv2.rectangle(frame, (faces[i][0], faces[i][1]), (faces[i][0]+faces[i][2], faces[i][1]+faces[i][3]),
                              (0, 0, 255, 2))

        # диктант
        if len(faces) == 0 and len(faces_data) != 0:
            for i in range(len(faces_data)):
                faces_data[i][-2] += int((time.time() % 10000)) - faces_data[i][-1]
                faces_data[i][-1] = int((time.time() % 10000))

        cv2.imwrite('face.png', frame)
        cv2.imshow("video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        for i in range(len(faces_data)):
            faces_data[i][4] = True
            faces_data[i][-1] = int(time.time() % 10000)

        print(faces_data)

    cap.release()
    cv2.destroyAllWindows()
