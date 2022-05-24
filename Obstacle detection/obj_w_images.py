import cv2 as cv
import numpy as np
import glob

image = #add path to image

try:
    img = cv.imread(image)

    height = int(img.shape[0])
    width = int(img.shape[1])

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([25, 50, 0])
    upper_red = np.array([70, 255, 255])

    mask = cv.inRange(hsv, lower_red, upper_red)
    mask_not = cv.bitwise_not(mask)
    cv.imshow("maks", mask_not)

    contours, _ = cv.findContours(mask_not, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    #cv.rectangle(img, (int(width/5), int(4*height/5)), (int(4*width/5), height), (255, 255, 0), 2)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv.drawContours(img, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(c)
        M = cv.moments(c)
        area = h*w
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the biggest contour (c) in green
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(img, (cX, cY), 5, (0, 0, 255), thickness=-1)

    if ((int(width / 5) < x < int(4 * width / 5)) or (int(width / 5) < (x + w) < int(4 * width / 5))) and (
            (y + h) > int(4 * height / 5)):
        print('ruh ro raggy')


except ZeroDivisionError as error:
    cX = 0
    cY = 0

cv.imshow('test', img)

cv.waitKey(0)
