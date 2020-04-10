# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:03:15 2020

@author: Darshit.Purohit
"""

import cv2

def divide(img):
#    print(int(img))

#    image = cv2.imread(img) #getting image
    image = img
    s=image.shape #size
    
    # Horizontal 
    imCrop1 = image[0:s[0], 0:int(s[1]/2)] #croping 1st part
    imCrop2 = image[0:s[0], int(s[1]/2):s[1]] #croping 2nd part
    
#    #Vertical
#    imCrop1 = image[0:int(s[0]/2), 0:s[1]]
#    imCrop2 = image[int(s[0]/2):s[0], 0:s[1]]
#    
    return imCrop1, imCrop2
    
#divide('Output/frame0.jpg')