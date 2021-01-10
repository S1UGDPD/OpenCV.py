# AIM : get the image of the Queen card and transform it as flat as possible

import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

# define the (float) array pixel point of Queen card
pts1 = np.float32( [ [228,45],[395,105],[143,276],[308,339] ] )


# define the array pixel point of casual card
# the width of card is 2,5inc, and the height is 3,5inc (keep the aspec ratio)
width, height = 250, 350
pts2 = np.float32( [ [0,0], [width,0],[0,height],[width, height] ] )


# .getPerspectiveTransform() : matrix that transform the first point of pixel to second point of pixel
#                              arguments: source, destination
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# .warpPerspective : operation to transform the perspective
#                    arguments: source, matrix, dsize
imgTransform = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("original", img)
cv2.imshow("transformed", imgTransform)
cv2.waitKey(0)