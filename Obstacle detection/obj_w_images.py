import cv2 as cv
import numpy as np

image = #add file path to image

try:
    img = cv.imread(image)

    height = int(img.shape[0])
    width = int(img.shape[1])

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower_green = np.array([25, 50, 0])
    upper_green = np.array([70, 255, 255])

    mask = cv.inRange(hsv, lower_green, upper_green)
    mask_not = cv.bitwise_not(mask)

    contours, _ = cv.findContours(mask_not, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        c = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(c)
        M = cv.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(img, (cX, cY), 5, (0, 0, 255), thickness=-1)

except ZeroDivisionError as error:
    cX = 0
    cY = 0

cv.imshow('Image', img)

cv.waitKey(0)
