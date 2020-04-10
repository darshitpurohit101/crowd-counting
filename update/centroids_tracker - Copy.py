# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:44:29 2020

@author: Darshit.Purohit
"""

from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker():
    def __init__(self, maxDisappeared=50):
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.maxDisappeared = maxDisappeared
        
    def register(self, centroids):
        self.objects[self.nextObjectID] = centroids
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1
        
    def deregister(self, objectID):
        del self.objects[objectID]
        del self.disappeared[objectID]
        
    def updates(self, rects):
        if len(rects) == 0:
            for objectID in list(self.disappeared.keys()):
                self.dissappeared[objectID] += 1
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)
            return self.objects
        
        inputCentroids = np.zeros((len(rects), 2), dtype = "int") #creates 2d list
        
        
        for i,cord in enumerate(rects):
                cX = int((cord[0] + cord[3]) / 2.0)
                cY = int((cord[1] + cord[2]) / 2.0)
#                print(cX, cY)
                inputCentroids[i] = (cX, cY)
#                print("inputcentroids: ",inputCentroids)
            
        if len(self.objects) == 0:    # if no uid exixst than register new
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i])
        
        else:
            print("ddd")
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())
            
            D = dist.cdist(np.array(objectCentroids), inputCentroids)
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]
            
            usedRows = set()
            usedCols = set()
            
            for (row, col) in zip(rows, cols):
                if row in usedRows or col in usedCols:
                    continue
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self.disappeared[objectID] = 0
                
                usedRows.add(row)
                usedCols.add(col)
                
            unusedRows = set(range(0,D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)
            
            if D.shape[0] >= D.shape[1]:
                for row in unusedRows:
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1
                    
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)
        
            else:
                 for col  in unusedCols:
                     self.registe(inputCentroids[col])
                     
#            print("this", self.objects)
            return self.objects
