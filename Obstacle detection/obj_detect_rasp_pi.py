from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import numpy as np

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

obj_detect = False

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    try:
        img = frame.array

        height = int(img.shape[0])
        width = int(img.shape[1])

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower_green = np.array([25, 50, 0])
        upper_green = np.array([70, 255, 255])

        mask = cv.inRange(hsv, lower_green, upper_green)
        mask_not = cv.bitwise_not(mask)
        cv.imshow("maks", mask_not)

        contours, _ = cv.findContours(mask_not, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            # find the biggest countour (c) by the area
            c = max(contours, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(c)
            M = cv.moments(c)
            area = h*w
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.circle(img, (cX, cY), 5, (0, 0, 255), thickness=-1)

        if ((int(width / 5) < x < int(4 * width / 5)) or (int(width / 5) < (x + w) < int(4 * width / 5))) and (
                (y + h) > int(4 * height / 5)):
            obj_detect = True
        else:
            obj_detect = False

        rawCapture.truncate(0)

    except ZeroDivisionError as error:
        cX = 0
        cY = 0

    cv.imshow('Obstacle detection', frame)

    cv.waitKey(0)
