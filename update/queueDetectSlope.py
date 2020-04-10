# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:19:54 2020

@author: Darshit.Purohit
"""
'''                                     USING SLOPE                            '''
#import dataentry
class Detect:
    def __init__(self):
        self.key_count = 0
        self.seq_count = 2
        self.next_count = 1
        self.min_slope = 1.5
        self.flag = True
        self.seq = []
        self.slope = []
        
    def key_values(self,cent):
        self.cent_lst = cent
        self.cent_key = cent[self.key_count]
#        print(self.cent_key)
        self.cal_dist()
        return self.seq
#        print(self.seq)
#        return self.seq
    
    def cal_dist(self):
        seq_count = self.seq_count
        next_count = self.next_count
        slope = ((self.cent_lst[next_count][1]-self.cent_lst[self.key_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[self.key_count][0]))
        if 1.5 > slope > 0 :
            self.seq.append(self.cent_lst[self.key_count])
            self.slope.append(slope)
#            print("initial seq ",self.seq)
            print(self.slope)
            while self.flag:
                slope = ((self.cent_lst[next_count][1]-self.cent_lst[seq_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[seq_count][0]))
#                self.slope.append(slope)
                if 1.5 > slope > 0:
                    self.seq.append(self.cent_lst[next_count])
                    self.slope.append(slope)
                    if seq_count != len(self.cent_lst)-1:
                        seq_count += 1
                    if next_count < seq_count:
                        next_count += 1
                    if seq_count == next_count:
                            self.seq.append(self.cent_lst[next_count])
                            self.slope.append(slope)
#                            print("last seq ",self.seq)
#                            print("last slope ",self.slope)
                            self.flag = False
#                    print('first seq ',self.seq)
#                    print('first slope ',self.slope)
                    print(next_count, seq_count)
#                    
                elif 1.5 < slope or slope < 0 :
#                    print("False")
                    self.next_cent(seq_count, next_count)
                    self.flag = False
#                    return self.seq
#            
#             
                
    def next_cent(self, seq_count, next_count):
        if seq_count != len(self.cent_lst)-1:
        		seq_count += 1
        slope = ((self.cent_lst[next_count][1]-self.cent_lst[seq_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[seq_count][0]))
        if 0 < slope < 1.5:
            self.seq.append(self.cent_lst[next_count])
            self.slope.append(slope)
#            print('next seq ',self.seq)
#            print('next slope ',self.slope)
            next_count = seq_count
            if seq_count != len(self.cent_lst)-1:
                seq_count += 1
            #    to check if seq_count != next_count
                while self.flag:
                
                    slope = ((self.cent_lst[next_count][1]-self.cent_lst[seq_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[seq_count][0]))
                    if 0 < slope < 1.5:
                        self.seq.append(self.cent_lst[next_count])
                        self.slope.append(slope)
                        if seq_count != len(self.cent_lst)-1:
                            seq_count += 1
                        if next_count < seq_count:
                            next_count += 1
                        if seq_count == next_count:
                            self.seq.append(self.cent_lst[next_count])
                            self.slope.append(slope)
#                            print("next last seq ",self.seq)
#                            print("next last slope ",self.slope)
                            self.flag = False
#                        print('next first seq ',self.seq)
#                        print('next first slope ',self.slope)
                        print(next_count, seq_count)
                    elif slope < 0 or slope > 1.5:
                        self.next_cent(seq_count, next_count)
                        self.flag = False
                    
            else:
                self.seq.append(self.cent_lst[next_count])
#                print("next last seq ",self.seq)
#import math
##import collections
#class Detect:
#    def __init__(self):
#        self.key_count = 0
#        self.seq_count = 2
#        self.next_count = 1
#        self.last = 0
#        self.flag = True
#        self.min_dist = 65
#        self.seq = []
#        self.seq_pre = []
#        
#        
#    def key_value(self, cent):
#    	self.cent_lst = cent
#    	self.cent_key = cent[self.key_count]
#        print(self.cent_key)
#    	self.cal_dist()
#        
#    def cal_dist(self):
#    	seq_count = self.seq_count
#    	next_count = self.next_count
#    	c = math.sqrt((self.cent_lst[next_count][0]-self.cent_lst[self.key_count][0])**2 + (self.cent_lst[next_count][1]-self.cent_lst[self.key_count][1])**2)
#    	if c<=self.min_dist:
#    		while self.flag:
#    			c = math.sqrt((self.cent_lst[self.key_count+seq_count][0]-self.cent_lst[self.key_count+next_count][0])**2 + (self.cent_lst[self.key_count+seq_count][1]-self.cent_lst[self.key_count+next_count][1])**2)
#    			if c <= self.min_dist:
#    				self.seq.append(self.cent_lst[self.key_count+next_count])
#    				if seq_count != len(self.cent_lst):
#    					seq_count += 1
#    				if self.next_count < self.seq_count:
#    					next_count += 1
#    			elif c > self.min_dist:
#    				self.seq = self.next_cent(seq_count, next_count)
#    				return self.seq
#    				self.flag = False
#    			elif c == 0 :
#    				self.flag = False
#    				return self.seq
#    	elif c>self.min_dist:
#    		self.next_keycent(next_count)
#            
#        
#    def next_cent(self, seq_count, next_count):
#        	if self.seq_count != len(self.cent_lst)-1:
#        		seq_count += 1
##        	self.flag = True
##        	while self.flag:
##        		c = math.sqrt((self.cent_lst[self.key_count+seq_count][0]-self.cent_lst[self.key_count+next_count][0])**2 + (self.cent_lst[self.key_count+seq_count][1]-self.cent_lst[self.key_count+next_count][1])**2)
##        		if c <=self.min_dist:
###        			if seq_count != len(self.cent_lst)-1:
###        				seq_count += 1
###        			if (next_count+2) < seq_count:
###        				if(next_count+1) == seq_count:
###        					next_count += 1
###        				next_count += 2
###                    self.flag = False
##        			self.seq.append(self.cent_lst[self.key_count+next_count])
##
##        
##        		elif c>self.min_dist:
##        			self.flag=False
##        			self.next_cent(seq_count,next_count)	
##        
##        		elif c == 0:
##        			self.flag = False
#        			return self.seq
#    
#    def next_keycent(self, next_count):
#    	self.next_count += 1
#    	self.next_count += 1
#    	self.cal_dist()	
	
#lst = [[843, 310], [893, 213]]        
#lst = [[744, 239], [792, 268], [843, 310], [893, 213], [957, 341], [1023, 380], [1044, 212], [1142, 437]]
#[[744, 239]]
#c = Detect()
#c.key_values(lst)