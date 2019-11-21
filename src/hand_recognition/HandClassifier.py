"""
:author: Ryan Nicholas
:date: November 21, 2019
:description: The purpose of this class is to updated the AI to recognize hands
"""

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
        :return:
        """
