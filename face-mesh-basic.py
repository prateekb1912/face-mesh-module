import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()

mpDraw = mp.solutions.drawing_utils

while True:
    _, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        print(results.multi_face_landmarks)
        for landmark in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, landmark, mpFaceMesh.FACE_CONNECTIONS)

    cv2.flip(img, 1)
    cv2.imshow("Face Mesh", img)

    if cv2.waitKey(1) == 27:
        break
