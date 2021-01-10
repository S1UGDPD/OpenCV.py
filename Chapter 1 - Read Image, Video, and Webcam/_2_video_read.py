## CHAPTER 1
## READ IMAGES - VIDEOS - WEBCAM

import cv2

# .VideoCapture
#               have an argument: the path of the video
cap = cv2.VideoCapture("resources/test-video.mp4")

# display the video by showing the frame one by one
while True:
    # 'success' variable will be a boolean true or false that tell us whether it was done succressfully or not
    # 'img' variable will save the image / frame one by one
    success, frame = cap.read()

    # show the result
    cv2.imshow('video', frame)

    # add the delay
    # and if 'q' is pressed, it will break the loop
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break