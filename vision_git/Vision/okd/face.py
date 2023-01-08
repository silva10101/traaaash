import cv2
import numpy as np


def delete_contours(contours, delete_list):
    delta = 0
    for i in range(len(delete_list)):
        # print("i= ", i)
        del contours[delete_list[i] - delta]
        delta = delta + 1
    return contours


cap = cv2.VideoCapture(0)


red_color_low = (170, 100, 100)
red_color_high = (180, 255, 255)

while True:
    ret, frame_or = cap.read()

    # cv2.imshow('FRAME', frame)
    frame = cv2.GaussianBlur(frame_or, (5, 5), 0)
    #  cv2.imshow('Blur', frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image = cv2.inRange(hsv, red_color_low, red_color_high)

    cv2.imshow('FILTER', image)

    contours, hierarchy = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        contours1 = list(contours)[0].tolist()

        x = contours1[0][0][0]
        y = contours1[0][0][1]
        l = round(len(contours1)/2)
        x_ = contours1[l][0][0]
        y_ = contours1[l][0][1]

        print(contours1[0][0])
        print(contours1[l][0])
        print(contours1)

        cv2.rectangle(frame_or, (x, y), (x_ , y_), (0, 255, 0), 2)

    # cv2.drawContours(frame_or, contours1[0], -1, (0, 255, 0), 1, cv2.LINE_AA, hierarchy, 1)
    # if len(contours1) != 0:
    #
    #     cv2.rectangle(frame_or, (x, y), (x + 20, y + 20), (0, 255, 0), 2)
    #
    cv2.imshow('contours', frame_or)
    # if len(contours1) != 0:
    #     print(contours1[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
