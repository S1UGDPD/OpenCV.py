import cv2, numpy as np
from stackImages import stackImages

def empty(a):
    pass

path = "resources/lambo.jpg"

# 2. create new window named track bars
#    set the color we need to white, and the color we dont need to black
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 43, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 60, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 95, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)

    # 1. convert into HSV space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 3. create trackbars position function to read trackbars values
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # 4. create a mask to filter out our images
    lower = np.array( [h_min, s_min, v_min] )
    upper = np.array( [h_max, s_max, v_max] )
    mask = cv2.inRange(imgHSV, lower, upper)

    # 5. creating an image as result
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    imgStack = stackImages(0.3, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stack", imgStack)

    cv2.waitKey(1)