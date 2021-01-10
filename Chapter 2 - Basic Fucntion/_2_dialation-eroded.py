import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
kernel = np.ones((5, 5), np.uint8)    # create 5x5 of one values matrix with range from 0 to 255

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(imgGray, 100, 100)
cv2.imshow("Clanny Image", imgCanny)


# .dialation : increase the thickness of edge so that there is no gap / not join properly
#              have arguments: object, kernel, and the number of iteration
#                    KERNEL::
#                    matrix that we have define the size & values
#                    using numpy to add the kernel
#                    ITERATION::
#                    how many iterations we want the cernel to move
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
cv2.imshow("Dialation Image", imgDialation)


# .erode : make an img thinner, in this case is the "imgDialation"
#          opposite to dialation
#          have argiments same as dialation.
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)