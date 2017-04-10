import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	cv2.imshow('original',frame)
	cv2.imshow('Laplacian',laplacian)
	edges = cv2.Canny(frame,100,100)
	cv2.imshow('edges',edges)
	k=cv2.waitKey(5)
	if k==27:
		break

cv2.destroyAllWindows()
cap.release()
