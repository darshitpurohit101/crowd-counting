# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:47:46 2020

@author: Darshit.Purohit
"""


import cv2
import sys
import yolo
import divide
import Roi_selection
import csv
 
(major_ver, minor_ver, subminor_ver) = (4, 1, 2)
 

def track(path): 
    path = path
 
#        i = int(input("enter"))
    
#        tracker = cv2.TrackerBoosting_create()

    tracker = cv2.TrackerMIL_create()

#        tracker = cv2.TrackerKCF_create()

#        tracker = cv2.TrackerTLD_create()

#        tracker = cv2.TrackerMedianFlow_create()

#        tracker = cv2.TrackerGOTURN_create()

#        tracker = cv2.TrackerMOSSE_create()

#        tracker = cv2.TrackerCSRT_create()
 
    # Read video
    video = cv2.VideoCapture(path)
 
    # Exit if video not opened.
    if not video.isOpened():
        print ("Could not open video")
        sys.exit()
 
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print ('Cannot read video file')
        sys.exit()
     
    # Define an initial bounding box
#    bbox = (287, 23, 86, 320)  # bounding box should be given heress

     
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
 
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()
 
        # Update tracker
        ok, bbox = tracker.update(frame) #create new bbox
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
        # Draw bounding box
        if ok:  # tracked box
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
     
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
        # Display result
        cv2.imshow("Tracking", frame)
 
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break