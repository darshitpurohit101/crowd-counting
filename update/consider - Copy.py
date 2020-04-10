# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:24:17 2020

@author: Darshit.Purohit
"""


def area(x1, y1, x2, y2, x3, y3): 
      
    return abs((x1 * (y2 - y3) + 
                x2 * (y3 - y1) + 
                x3 * (y1 - y2)) / 2.0) 

def check(x1, y1, x2, y2, x3, y3, x4, y4, x, y): 
                
    # Calculate area of rectangle ABCD  
    A = (area(x1, y1, x2, y2, x3, y3) +
         area(x1, y1, x4, y4, x3, y3)) 
  
    # Calculate area of triangle PAB  
    A1 = area(x, y, x1, y1, x2, y2) 
  
    # Calculate area of triangle PBC  
    A2 = area(x, y, x2, y2, x3, y3) 
  
    # Calculate area of triangle PCD  
    A3 = area(x, y, x3, y3, x4, y4) 
  
    # Calculate area of triangle PAD  
    A4 = area(x, y, x1, y1, x4, y4); 
  
    # Check if sum of A1, A2, A3  
    # and A4 is same as A  
    if A == (A1 + A2 + A3 + A4) :
        return 1
    else: 
        return 0

  