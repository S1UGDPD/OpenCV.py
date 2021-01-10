import cv2, numpy as np
from stackImages import stackImages

# 2. find the edges
def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # for each contour, we are going to find the area fest
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        # draw the contour to 'imgContour' if area is greater than 500px
        # .drawContours() : image, contours, contourIndex, color, thickness
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # length of each contour arc by arc
            peri = cv2.arcLength(cnt, True)
            print(peri)
            # get the point of corner point
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(approx)
            # create object corner / bounding boxes
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # categorize the object
            if objCor == 3: objectType = "Triangle"
            elif objCor == 4:
                aspecRatio = w/float(h)
                if aspecRatio > 0.95 and aspecRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4: objectType = "Circle"
            else: objectType = "None"
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, ( x+(w//2)-10, y+(h//2)-10 ), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255,0), 2)


path = "resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()

# 1. preproccess the image first: convert into a grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContour(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.5, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]))


cv2.imshow("Output", imgStack)
cv2.waitKey(0)