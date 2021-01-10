## CHAPTER 1
## READ IMAGES - VIDEOS - WEBCAM

# import the library
import cv2
print("Package Imported")

# .imread() to read an image
#           have an argument: location of the image
img = cv2.imread("resources/test_img.jpg")

# .imshow() to show the image
#           have two arguments: "output name" and 'image to show'
cv2.imshow("image", img)

# .waitKey to delay the show
#          have an argumen: time in milisecons, 0 for infinite
cv2.waitKey(0)

# .write ??
# cv2.write()