# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 09:44:22 2019

@author: Darshit.Purohit
"""

import cv2

f = cv2.VideoCapture('C://Users//Darshit.Purohit//Downloads//SharpView CCTV in Shopping Mall.mp4')
while True:
    ret, frame = f.read()
    cv2.imshow('title', frame)
    if cv2.waitKey(60) == 27:
        break
cv2.destroyAllWindows() 

#while True:
#    ret, frame = f.read()
#    cv2.imshow('title',frame)
#    

#    
#cv2.distroyAllWindows()
