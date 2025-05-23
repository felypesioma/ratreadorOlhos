import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=True)

    if faces:
        face = faces[0]
        
        left_eye = face[159]
        right_eye = face[386]
        left_center = face[468]
        right_center = face[473]  

        cv2.circle(img, left_center, 5, (0,255,0), cv2.FILLED)
        cv2.circle(img, right_center, 5, (0,255,0), cv2.FILLED)
        left_eye_ratio = (left_center[0] - left_eye[0])
        right_eye_ratio = (right_center[0] - right_eye[0])

        if left_eye_ratio < -5 and right_eye_ratio < -5:
            cv2.putText(img, 'Looking Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        elif left_eye_ratio > 5 and right_eye_ratio > 5:
            cv2.putText(img, 'Looking Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        else:
            cv2.putText(img, 'Looking Center', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
