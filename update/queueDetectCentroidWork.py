# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:19:54 2020

@author: Darshit.Purohit
"""
import math
class Detect:
    def __init__(self):
        self.key_count = 0
        self.seq_count = 2
        self.next_count = 1
        self.min_dist = 95
        self.flag = True
        self.seq = []
        self.c = []
        
    def key_values(self,cent):
        self.cent_lst = cent
        self.cent_key = cent[self.key_count]
#        print(self.cent_key)
        self.cal_dist()
#        print(self.seq)
#        return self.seq
    
    def cal_dist(self):
#        seq_count = self.seq_count
        next_count = self.next_count
        c = math.sqrt((self.cent_lst[next_count][0]-self.cent_lst[self.key_count][0])**2 + (self.cent_lst[next_count][1]-self.cent_lst[self.key_count][1])**2)
        print(c)
#        if c < self.min_dist:
#            self.seq.append(self.cent_lst[self.key_count])
#            print(self.seq)
#            self.slope = ((self.cent_lst[next_count][1]-self.cent_lst[self.key_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[self.key_count][0]))
#            print(self.slope)
###            self.c.append(c)
#            while self.flag:
#                
#                c = math.sqrt((self.cent_lst[seq_count][0]-self.cent_lst[next_count][0])**2 + (self.cent_lst[seq_count][1]-self.cent_lst[next_count][1])**2)
#                self.c.append(c)
#                if c != 0 and c <= self.min_dist:
#                    self.seq.append(self.cent_lst[next_count])
#                    if seq_count != len(self.cent_lst)-1:
#                        seq_count += 1
#                    if next_count < seq_count:
#                        next_count += 1
#                    print(self.seq)
#                    print(next_count, seq_count)
#                    
#                
#                elif c >self.min_dist:
#                    print("False")
#                    self.flag = False
#                    
#                elif c == 0:
#                    self.seq.append(self.cent_lst[next_count])
#                    self.flag = False
#                    return self.seq
#            
#             
                
#    def next_cent(self):
        
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
##        	if self.seq_count != len(self.cent_lst)-1:
##        		seq_count += 1
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
	
lst = [[843, 310], [957, 341]]        
#lst =  [[115, 449], [190, 452], [268, 451], [311, 451], [388, 454], [441, 451], [491, 448], [538, 445], [575, 443], [609, 424], [677, 424], [729, 443], [806, 443], [869, 441], [940, 447], [998, 450], [1067, 445]]
#[[744, 239]]
c = Detect()
c.key_values(lst)