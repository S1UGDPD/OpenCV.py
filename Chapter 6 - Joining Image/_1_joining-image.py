import cv2
import numpy as np


img = cv2.imread('resources/lena.png')

# .hstack : horizontal stack function
# .vstack : vertical stack function
#           arguments: object to stack
imgHor = np.hstack( (img, img) )
imgVer = np.vstack( (img, img) )

cv2.imshow("original", img)
cv2.imshow("H-stack", imgHor)
cv2.imshow("V-stack", imgVer)

cv2.waitKey(0)