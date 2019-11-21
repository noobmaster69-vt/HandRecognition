"""
:author: Ryan Nicholas
:date: November 21, 2019
:description: The purpose of this class is to updated the AI to recognize hands
"""

import cv2 as cv

class HandClassifier:
    def __init__(self, picture):
        """
        Constructor
        """
        self.k = 0
        self.pic = picture

    def processImage(self):
        """
        Process the image and recognize the hand portion of the code
        :return: none
        """
        gray = cv.cvtColor(self.pic, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5, 5), 0)
        ret, thresh = cv.GaussianBlur(blur, (5, 5), 0)
        cv.imshow('Black and White', thresh)
        return blur
