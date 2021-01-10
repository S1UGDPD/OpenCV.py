import cv2, numpy as np

# add our cascade
faceCascade = cv2.CascadeClassifier("C:/Users/AGIT/AppData/Local/Programs/Python/Python38-32/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

path = "resources/lena.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find the faces of this image using our face cascade
# .detecMultiScale() : img, scaleFactors, minimumNeighbor
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# create a bounding boxes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)