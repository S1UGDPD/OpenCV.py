import cv2
import numpy as np

# make an zeros matrix with size of 512x512 BGR with values 0 to 255
img = np.zeros((512, 512, 3), np.uint8)

# .putText() : add text to image
#              arguments: img, *text, org (location), fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin
cv2.putText(img, " OPENCV ", (150, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

# show the image
cv2.imshow("Image", img)
cv2.waitKey(0)