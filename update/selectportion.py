# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:58:22 2020

@author: Darshit.Puro
"""
#import numpy as np 
#import cv2

#
#def area(x1, y1, x2, y2, x3, y3): 
#      
#    return abs((x1 * (y2 - y3) + 
#                x2 * (y3 - y1) + 
#                x3 * (y1 - y2)) / 2.0) 
#
#def check(x1, y1, x2, y2, x3,  
#          y3, x4, y4, x, y): 
#                
#    # Calculate area of rectangle ABCD  
#    A = (area(x1, y1, x2, y2, x3, y3) +
#         area(x1, y1, x4, y4, x3, y3)) 
#  
#    # Calculate area of triangle PAB  
#    A1 = area(x, y, x1, y1, x2, y2) 
#  
#    # Calculate area of triangle PBC  
#    A2 = area(x, y, x2, y2, x3, y3) 
#  
#    # Calculate area of triangle PCD  
#    A3 = area(x, y, x3, y3, x4, y4) 
#  
#    # Calculate area of triangle PAD  
#    A4 = area(x, y, x1, y1, x4, y4); 
#  
#    # Check if sum of A1, A2, A3  
#    # and A4 is same as A  
#    return (A == A1 + A2 + A3 + A4) 
#
#
#if __name__ == '__main__': 
#      
#    # Let us check whether the point  
#    # P(10, 15) lies inside the  
#    # rectangle formed by A(0, 10), 
#    # B(10, 0) C(0, -10) D(-10, 0)  
#    if (check(0, 240, 530, 240, 530, 159,  
#                    0, 165, 133, 211 )): #(cordinates,x,y) 
#        print("yes") 
#    else: 
#        print("no") 



im = cv2.imread('foreground.jpg')

#height,width,depth = im.shape

#draws a shape based on dimensions
shape = np.array([[[0,150], [576, 208], [576,300], [0,215]]], np.int32)
points = shape.reshape((-1, 1, 2))
ploy = cv2.polylines(im, [points], True, (0,255,255))

#mask = np.zeros(im.shape,np.uint8)


#res = cv2.bitwise_and(im, im, mask = shape)

cv2.imshow("masked", ploy)
cv2.imwrite('step/roiRect.jpg',ploy)
cv2.waitKey(0)
