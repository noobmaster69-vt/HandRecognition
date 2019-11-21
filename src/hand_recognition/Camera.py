"""
:author: Ryan Nicholas
:date: November 21, 2019
:description: This code communicates with the camera
"""

import cv2 as cv

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

            if cv.waitKey(1) == ord('q'):
                break
