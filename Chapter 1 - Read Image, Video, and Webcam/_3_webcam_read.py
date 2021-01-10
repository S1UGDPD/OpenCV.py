## CHAPTER 1
## READ IMAGES - VIDEOS - WEBCAM

import cv2

# change the value of argument by 0 for default webcam, or by webcam ID
cap = cv2.VideoCapture(0)
# ID number three for width
cap.set(3, 640)
# ID number four for height
cap.set(4, 480)
# ID number ten for brightness
cap.set(10, 100)


while True:
    success, frame = cap.read()
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break