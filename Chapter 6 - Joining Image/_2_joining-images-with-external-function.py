import cv2, numpy as np

from stackImages import stackImages

img = cv2.imread('resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# How to used "stackImages.py"
# 1. create an image stack
#    stackImages(scale, matrices of images)
imgStack = stackImages(0.5, ([img, img, img], [img, imgGray, img]))

cv2.imshow("original", img)
cv2.imshow("stack", imgStack)

cv2.waitKey(0)