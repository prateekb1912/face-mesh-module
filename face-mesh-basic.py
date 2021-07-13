import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()

while True:
    _, img = cap.read()

    cv2.flip(img, 1)
    cv2.imshow("Face Mesh", img)

    if cv2.waitKey(1) == 27:
        break
