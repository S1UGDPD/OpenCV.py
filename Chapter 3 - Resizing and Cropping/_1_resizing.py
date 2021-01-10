import cv2
import numpy as np

img = cv2.imread("resources/sample.jpg")

# find the size for image above
# obj.shape : chek the shape of our image
#             the first output - height
#                 second output - width
#                 third output - channels (3 for RGB)
print( img.shape )
cv2.imshow("Original", img)


# .resize() : resizing the image, increasing the number of pixel but not in quality
#             arguments: object to resize and width-height in brackets
imgResize = cv2.resize(img, (1000, 500))
print( imgResize.shape )
cv2.imshow("Resized", imgResize)


cv2.waitKey(0)