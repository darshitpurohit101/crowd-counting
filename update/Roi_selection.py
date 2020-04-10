# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:04:18 2020

@author: Darshit.Purohit
"""
import cv2
import numpy as np

def roi(path):
#    img = cv2.imread(path)    
    original_image = path
    (h, w) = original_image.shape[:2]
    
    (cX, cY) = (320.0, 278.0)
    
    angle = 20
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
#    cos = np.abs(M[0, 0])
#    sin = np.abs(M[0, 1])
    
#    nW = int((h * sin) + (w * cos))
#    nH = int((h * cos) + (w * sin))
    nW = 762
    nH = 702
    
    # Adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    #        print('M: ',M)
    
    # Perform the actual rotation and return the image
    clone = cv2.warpAffine(original_image, M, (nW, nH))
#    cv2.imshow('defualt',clone)
    cv2.imwrite('Output/rotated.jpg', clone)
    return clone

#roi('D:/Queue Managment/Dataset/crop2.jpg')