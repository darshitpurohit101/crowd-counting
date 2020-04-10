# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:45:31 2019

@author: Darshit.Purohit
"""
#
import cv2
import gui
import numpy as np
 
def draw(image):
    im = image

    cv2.imwrite('crop.jpg',im)
    r = cv2.selectROI(im)
        
    img = cv2.rectangle(im,r,(0,255,0),2)

    cv2.destroyAllWindows()
    
    return r, img
#    cv2.imshow("Image", img)
#    cv2.imwrite('foreground.jpg',img)
#

#    
    
    
