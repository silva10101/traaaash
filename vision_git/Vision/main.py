import cv2
from smbus import SMBus
import numpy as np
import threading


class controller(object):
    __servoHorizontal = 0
    __servoVertical = 0

    def sendData(self, data):
        bus = SMBus(1)
        time.sleep(1)
        bus.write_i2c_block_data(0x39, 0x00, data)
        bus.close()
        time.sleep(0.1)

    def __init__(self):
        self.__servoHorizontal = 90
        self.__servoVertical = 45

    def ServoSetPosition(self, servo1, servo2):
        if servo1 < 0:
            self.__servoHorizontal = 0
        elif servo1 > 180:
            self.__servoHorizontal = 180
        else:
            self.__servoHorizontal = servo1
        if servo2 < 0:
            self.__servoVertical = 0
        elif servo2 > 180:
            self.__servoVertical = 180
        else:
            self.__servoVertical = servo2

    def GetPosition(self):
        position = [self.__servoHorizontal, self.__servoVertical]
        return position


class package(object):
    __data = []

    def getData(self, data):
        if len(data) > 8:
            return -1
        self.__data = []
        for i in data:
            if i < 255:
                self.__data.append(i)
            else:
                return -1
        return 1

    def returnData(self):
        data = self.__data
        return data


arduino = controller()

package = package()

from picamera import PiCamera
from picamera.array import PiRGBArray

import time

middle = (320, 240)
center = [320, 240]
arduino.sendData(arduino.GetPosition());
delta = 2
errOld = 0
kp = 0.132
kd = -0.04
ki = 0.0001


def position():
    global center
    while True:
        i = 0
        while (abs(center[0] - middle[0]) > 20):
            flag = center[0] > middle[0]
            error = abs(center[1] - middle[1])
            p = error * kp
            d = kd * (error - errOld)
            i += ki * error
            u = int(p + i + d)
            print(u)
            if flag:
                position = arduino.GetPosition()
                position[0] = position[0] + u
                arduino.ServoSetPosition(position[0], position[1]);
                arduino.sendData(arduino.GetPosition())
            else:
                position = arduino.GetPosition()
                position[0] = position[0] - u
                arduino.ServoSetPosition(position[0], position[1]);
                arduino.sendData(arduino.GetPosition())
        i = 0
        while (abs(center[1] - middle[1]) > 20):
            error = abs(center[1] - middle[1])
            p = error * kp
            d = kd * (error - errOld)
            i += ki * error
            u = int(p + i + d)
            print(u)
            flag = center[1] > middle[1]
            if flag:
                position = arduino.GetPosition()
                position[1] = position[1] - u
                arduino.ServoSetPosition(position[0], position[1]);
                arduino.sendData(arduino.GetPosition())
            else:
                position = arduino.GetPosition()
                position[1] = position[1] + u
                arduino.ServoSetPosition(position[0], position[1])
                arduino.sendData(arduino.GetPosition())


th = threading.Thread(target=position)
th.start()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
image = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    image = cv2.flip(image, 0)
    red_color_low = (170, 100, 100)
    red_color_high = (180, 255, 255)
    frame = image.copy()
    frame_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    stop_simbol = cv2.inRange(frame_hsv, red_color_low, red_color_high)
    moments = cv2.moments(stop_simbol, 1)
    area_stop = moments['m00']
    if area_stop != 0:
        (cnts, data) = cv2.findContours(stop_simbol.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        rect = cv2.minAreaRect(c)
        center = (int(rect[0][0]), int(rect[0][1]))
        box = np.int0(cv2.boxPoints(rect))
        cv2.putText(frame, str(center[0]) + ',' + str(center[1]), center, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                    2)
        cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)

    cv2.imshow("Binary", stop_simbol)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame

    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop

    if key == ord("q"):
        break
    elif key == ord("c"):
        pass





