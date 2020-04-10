# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:15:48 2020

@author: Darshit.Purohit
"""
from scipy.spatial import distance


unique_person = dict()
personID = 1
euclidean_distance = dict()
frame_no = 0
not_detected = dict()

def track(x1, y1 , x2, y2, frame):
    global unique_person
    global personID 
    global euclidean_distance
    global frame_no
    global not_detected
    
    cx, cy = (x1 + x2)/2, (y1 + y2)/2 #finding centroid

    if frame == 0:
    
        unique_person[personID] = [cx,cy]
        not_detected[personID] = 0
        
        personID += 1
        
        print('frist', cx, cy)
    
    else:
        if frame > frame_no:
            frame_no = frame
            euclidean_distance.clear()
            
        new_centroid = [cx, cy]
        
        for uid, centroid in unique_person.items():
            dist = distance.euclidean(centroid, new_centroid)
            euclidean_distance[uid] = dist
        print(euclidean_distance)
            
            

        
        
            
            
        
        