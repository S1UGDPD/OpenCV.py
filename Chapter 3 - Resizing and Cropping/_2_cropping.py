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

# basically, image is an array of pixel
# so to cropping an image we can add square brackets with argument 'height-width'
# same as we do the array-slicing
imgCropped = img[25:100, 50:]
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)

# NOTE THAT IN OPEN CV, THE SEQUENCE IS 'WIDTH-HEIGHT'
# BUT IN THE PYTHON DEFAULT, THE SEQUENCE IS 'HEIGHT-WIDTH'