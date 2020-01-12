# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:46:01 2019

@author: Darshit.Purohit
"""
import frame

option = int(input("Input '0' to use webcam and '1' to give video as input : "))
if option == 1:
    video_file = input("Enter video file path: ")
elif option == 0:
    video_file = 0
    
threshold = int(input("Alert me if crowd count goes beyond : "))
maxpeople = threshold
#create image frame by frame
frame.frame_creator(video_file, maxpeople)
