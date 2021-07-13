import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    cv2.flip(img, 1)

    cv2.imshow("Face Mesh", img)

    if cv2.waitKey(1) == 27:
        break
