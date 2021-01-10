import cv2
import numpy as np

# make an zeros matrix with size of 512x512 BGR with values 0 to 255
img = np.zeros((512, 512, 3), np.uint8)

# print the detail of the image
print( img.shape )
print( img )


# coloring the image
img[:] = 0, 0, 0


# .line() : draw a line in the image
#           arguments: ( img, plt1, plt2, color, thickness, lineType, shift )
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)
#                           width - height


# .rectangle() : draw a rectangle in the image
#                arguments: ( img, plt1, plt2, color, thickness, lineType, shift )
cv2.rectangle(img, (256,256), (512, 512), (255,255,255), 3)
cv2.rectangle(img, (0,0), (50,50), (0,0,255), cv2.FILLED)


# .circle() : draw a circle in the image
#             arguments ( img, center, radius, color, thickness, lineType, shift )
cv2.circle(img, (256,256), 50, (255,255,0), 3)


# show the image
cv2.imshow("Image", img)
cv2.waitKey(0)