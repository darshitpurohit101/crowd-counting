import cv2
import numpy as np

class cordinates:
    def __init__(self):
        
        self.cropping = False
        self.x_start, self.y_start, self.x_end, self.y_end = 0, 0, 0, 0
        self.refPoint = 0

    def mouse_crop(self, event, x, y, flags, param):

        self.oriImage = self.image.copy()
    
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x_start, self.y_start, self.x_end, self.y_end = x, y, x, y
            self.cropping = True
 
    # Mouse is Moving
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.cropping == True:
                self.x_end, self.y_end = x, y
 
    # if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates
            self.x_end, self.y_end = x, y
            self.cropping = False # cropping is finished
 
            self.refPoint = [(self.x_start, self.y_start), (self.x_end, self.y_end)]
 
            if len(self.refPoint) == 2: #when two points were found
#                roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
#                cv2.imshow("Cropped", roi)
                self.c = False
                
    def cord(self, img):
        self.image = img
        self.c = True
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.mouse_crop)
        while self.c:
 
            i = self.image.copy()
 
            if not self.cropping:
                cv2.imshow("image", self.image)
 
            elif self.cropping:
                cv2.rectangle(i, (self.x_start, self.y_start), (self.x_end, self.y_end), (255, 0, 0), 2)
                cv2.imshow("image", i)
 
            cv2.waitKey(1)
# close all open windows
        cv2.destroyAllWindows()
        return self.refPoint
#
#img = cv2.imread('D:/Queue managment v1/step/first.jpg')
#t = cordinates()
#t.cord(img)        
            

    
    
    
