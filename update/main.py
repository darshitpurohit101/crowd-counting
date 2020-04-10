# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:46:01 20195

@author: Darshit.Purohit
"""
import frame
import crop2
import cv2

option = int(input("Input '0' to use webcam and '1' to give video as input : "))
if option == 1:
    video_file = input("Enter video file path: ")
elif option == 0:
    video_file = 0
    
threshold = int(input("Alert me if crowd count goes beyond : "))
maxpeople = threshold
#create image frame by frame
cap= cv2.VideoCapture(video_file)
ret, frame1 = cap.read()
t = crop2.cordinates()
r = t.cord(frame1)
frame.frame_creator(video_file, maxpeople,r)
    
###
""" Use fixed length for bouding box """
###