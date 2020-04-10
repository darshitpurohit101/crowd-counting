# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 12:51:53 2019

@author: Darshit.Purohit
"""

import cv2

v = cv2.VideoCapture(0)

while (v.isOpened()):
    ret, frame = v.read()
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    
v.release()
cv2.destroyAllWindows()