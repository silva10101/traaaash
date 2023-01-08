import serial
import time
import cv2
import numpy

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

ArduinoSerial = serial.Serial('com3', 115200, timeout=.1)
time.sleep(2)
print(ArduinoSerial.readline())

print("connect")

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

    height, width = img.shape[:2]
    angle_w = 90 / width
    angle_h = 90 / height

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        shir = (x + w / 2) * angle_w
        shir = shir.astype(int)
        shir = shir.tobytes()

        vis = (y + h / 2) * angle_h
        vis = vis.astype(int) + 128
        vis = vis.tobytes()
        res = shir | vis

        READ_1 = int.from_bytes(ArduinoSerial.readline(), "big")
        if shir != READ_1:
            print('REad', READ_1)
            ArduinoSerial.write(res)
            print('writes', shir)
            print('writev', vis)

    cv2.imshow('rez', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
