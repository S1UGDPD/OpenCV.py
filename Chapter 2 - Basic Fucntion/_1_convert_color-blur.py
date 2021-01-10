import cv2

img = cv2.imread("resources/lena.png")
cv2.imshow("Original Image", img)

# using .cvtColor() to convert the color of image
#                   have two arguments: image to convert and convert mode
# convert into Grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)

# using .GaussianBlur() to blur the image
#                       have arguments: target image, key size, sigma X
imgBlur = cv2.GaussianBlur(imgGray, (9,9), 0)
cv2.imshow("Blur Image", imgBlur)

# using .Canny to find edges in the image
#              have arguments: target image, treshold1, treshold2
imgCanny = cv2.Canny(imgGray, 100, 100)
cv2.imshow("Clanny Image", imgCanny)

cv2.waitKey(0)