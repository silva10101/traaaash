import numpy
import cv2

cap = cv2.VideoCapture(0)

while True:
	print(help(cv2.GaussianBlur))
	r, f = cap.read()
	f = cv2.GaussianBlur(f, 0, 0)
	cv2.imshow('fffff', f)
	cv2.waitKey(10)