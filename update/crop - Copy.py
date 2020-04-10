# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:45:31 2019

@author: Darshit.Purohit
"""
#
import cv2
import gui
import numpy as np
 
if __name__ == '__main__' :
    # Read image
    im = cv2.imread("D:/Queue managment v1/step/first.jpg")
    # Select ROI
#    ims = cv2.resize(im, (800, 600))
#    cv2.imwrite('crop.jpg',im)
    
    def on_click(event, x, y, p1, p2):
        if event == cv2.EVENT_LBUTTONDOWN:
            
            print(x,y)
    
    cv2.selectROI('Frame', im, True, False)    
#    cv2.imshow("Frame",r)
    cv2.setMouseCallback("Frame", on_click)
#    gui.up(r[0])
#    print("from (height)",r[1],"to",int(r[1]+r[3]))
#    print("from (width)",r[0],"to",int(r[0]+r[2]))
    # Crop image
#    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
#    img = cv2.rectangle(im,r,(0,255,0),2)
#    img = cv2.line(im, (r[0],r[1]),(r[2],r[3]), (0,255,255), 2)
    
#    imCrop = im[124:251, 633:487]
    # Display cropped image
#    cv2.imshow("Image", img)
    
#    cv2.imwrite('foreground.jpg',imCrop)
#    cv2.resizeWindow('Image',500,500)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#i = 0
#for j in range(0,100):
#    if j%2 == 0:
#        gui.up(j
#
