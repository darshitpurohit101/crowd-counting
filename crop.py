# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:45:31 2019

@author: Darshit.Purohit
"""

import cv2
import gui
import numpy as np
 
if __name__ == '__main__' :
    # Read image
    im = cv2.imread("Output/frame0.jpg")
    # Select ROI
#    ims = cv2.resize(im, (800, 600))
    cv2.imwrite('crop.jpg',im)
    r = cv2.selectROI(im)
#    gui.up(r[0])
    print("from (height)",r[1],"to",int(r[1]+r[3]))
    print("from (width)",r[0],"to",int(r[0]+r[2]))
    # Crop image
    imCrop = imc[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
#    imCrop = im[371:1070, 12:1376]
    # Display cropped image
    cv2.imshow("Image", imCrop)
#    cv2.resizeWindow('Image',500,500)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
i = 0
#for j in range(0,100):
#    if j%2 == 0:
#        gui.up(j