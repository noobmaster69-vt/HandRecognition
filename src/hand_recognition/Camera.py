"""
:author: Ryan Nicholas
:date: November 21, 2019
:description: This code communicates with the camera
"""

import cv2 as cv
import numpy as np
import src.hand_recognition.HandClassifier as process

class Camera:
    """
    Camera Class
    """

    def __init__(self):
        """
        Constructor
        """
        self.cap = cv.VideoCapture(0)  # start capturing video
        if not self.cap.isOpened():
            print("Can not open camera")
            exit(0)
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # if frame is read correctly, ret is True
            if not ret:
                print("Cannot receive frame (stream end?). Exiting...")
                break
            if frame is None:
                print("No frame")
                break

            # Operations on the frame here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray, (5, 5), 0)
            ret, thresh1 = cv.threshold(blur, 70, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
            contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            max_area = 0
            ci = 0
            for i in range(len(contours)):
                cnt = contours[i]
                area = cv.contourArea(cnt)
                if area > max_area:
                    max_area = area
                    ci = i
            cnt = contours[ci]
            hull = cv.convexHull(cnt)

            drawing = np.zeros(frame.shape, np.uint8)
            cv.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)
            cv.drawContours(drawing, [hull], 0, (0, 0, 255), 2)

            cv.imshow('hand', thresh1)

            # quit the program
            if cv.waitKey(1) == ord('q'):
                break
        # close the camera
        self.cap.release()
        cv.destroyAllWindows()
