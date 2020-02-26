# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:19:54 2020

@author: Darshit.Purohit
"""
'''                                     USING SLOPE                            '''
import dataentry
class Detect:
    def __init__(self):
        self.key_count = 0
        self.seq_count = 2
        self.next_count = 1
        self.min_slope = 1.5
        self.flag = True
        self.seq = []
        self.slope = []
        self.miss_count = 0
        
    def key_values(self,cent):
        self.cent_lst = cent
        self.cent_key = cent[self.key_count]
#        print(self.cent_key)
        self.cal_dist()
        print(self.seq)
#        print(self.slope)
        dataentry.datawrite(self.seq,self.cent_lst)
        return self.seq
#        return self.seq
    
    def cal_dist(self):
        seq_count = self.seq_count
        next_count = self.next_count
#        print("check index ",seq_count,next_count)
        if self.cent_lst[next_count][0] == self.cent_lst[self.key_count][0]:
            self.miss_count = 0
            if len(self.seq) > 1:
                self.seq.append(self.cent_lst[self.key_count])
            return self.seq
        slope = ((self.cent_lst[next_count][1]-self.cent_lst[self.key_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[self.key_count][0]))
#        print(slope)
        if 1.5 > slope > -0.5 :
            self.miss_count = 0
            self.seq.append(self.cent_lst[self.key_count])
            self.slope.append(slope)
            print("initial seq ",self.seq)
#            print(self.slope)
            if seq_count == len(self.cent_lst):
                return self.seq
#            and self.seq_count >= len(self.cent_lst)-1 # it should be at line 53
            if next_count == seq_count :
                if self.seq_count >= len(self.cent_lst)-1:
                    self.seq.append(self.cent_lst[next_count])
                    print("new loop",self.seq)
                    self.flag = False
                else: # for moving the queue counter ahead
                    seq_count += 1
            while self.flag:
                slope = ((self.cent_lst[next_count][1]-self.cent_lst[seq_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[seq_count][0]))
#                self.slope.append(slope)
                if 1.5 > slope > -0.5:
                    self.seq.append(self.cent_lst[next_count])
                    self.slope.append(slope)
                    if seq_count != len(self.cent_lst)-1:
                        seq_count += 1
                    if next_count < seq_count:
                        next_count += 1
                    if seq_count == next_count:
                        print('count same: ',next_count,seq_count)
                        if len(self.seq) > 1:
                            slope = ((self.cent_lst[next_count][1]-self.cent_lst[next_count-1][1])/(self.cent_lst[next_count][0]-self.cent_lst[next_count-1][0]))
                            print('slope and nextcount: ',slope, next_count-1)
                            if 1.5 > slope > -0.5: 
                                self.seq.append(self.cent_lst[next_count])
                                self.slope.append(slope)
                                print("last seq ",self.seq)
#                            print("last slope ",self.slope)
                            self.flag = False
                    print('first seq ',self.seq)
#                    print('first slope ',self.slope)
#                    print(next_count, seq_count)
#                    
                elif 1.5 < slope or slope < -0.5 :
#                    print("False")
                    self.next_cent(seq_count, next_count)
                    self.flag = False
#                    return self.seq
                    
                elif slope == 0:
                     self.seq.append(self.cent_lst[next_count])
                     print('slope=0 ',self.seq)
                     self.slope.append(slope)
                     self.flag = False
         
        elif slope < -0.5 or slope > 1.5:
            self.miss_count += 1
            if self.miss_count == 2:
                if self.key_count < len(self.cent_lst)-1:
                    self.key_count += 1
                if self.next_count < len(self.cent_lst)-1:
                    self.next_count += 1
                if self.seq_count < len(self.cent_lst)-1:
                    self.seq_count += 1
                print("key",self.key_count)
            elif self.miss_count == 1:
                print('key=1')
                if self.next_count < len(self.cent_lst)-1:
                    self.next_count += 1
            elif self.miss_count > 2:
                return
            self.cal_dist()
                
    def next_cent(self, seq_count, next_count):
        if seq_count != len(self.cent_lst)-1:
        		seq_count += 1
        if self.cent_lst[next_count][0] == self.cent_lst[seq_count][0]:
            if len(self.seq) > 1:
                self.seq.append(self.cent_lst[next_count])
            return self.seq
        slope = ((self.cent_lst[next_count][1]-self.cent_lst[seq_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[seq_count][0]))
        print('verify: ',next_count, seq_count, slope)
        if -0.5 < slope < 1.5:
            self.seq.append(self.cent_lst[next_count])
            self.seq.append(self.cent_lst[seq_count])
            self.slope.append(slope)
            print('next seq ',self.seq)
#            print('next slope ',self.slope)
            next_count = seq_count
            if seq_count != len(self.cent_lst)-1:
                seq_count += 1
            #    to check if seq_count != next_count
                while self.flag:
                
                    slope = ((self.cent_lst[next_count][1]-self.cent_lst[seq_count][1])/(self.cent_lst[next_count][0]-self.cent_lst[seq_count][0]))
                    if -0.5 < slope < 1.5:
                        self.seq.append(self.cent_lst[next_count])
                        self.slope.append(slope)
                        if seq_count != len(self.cent_lst)-1:
                            seq_count += 1
                        if next_count < seq_count:
                            next_count += 1
                        if seq_count == next_count:
                            self.seq.append(self.cent_lst[next_count])
                            self.slope.append(slope)
                            print("next last seq ",self.seq)
#                            print("next last slope ",self.slope)
                            self.flag = False
                        print('next first seq ',self.seq)
#                        print('next first slope ',self.slope)
#                        print(next_count, seq_count)
                    elif slope < -0.5 or slope > 1.5:
                        self.next_cent(seq_count, next_count)
                        self.flag = False
                        
                    elif slope == 0:
                     self.seq.append(self.cent_lst[next_count])
                     self.slope.append(slope)
                     self.flag = False
                    
            else:
                self.seq.append(self.cent_lst[next_count])
                print("next last seq ",self.seq)
                
        else:
            self.miss_count += 1
            if self.miss_count == 2:
                if next_count < len(self.cent_lst)-1:
                    next_count += 1
                if seq_count < len(self.cent_lst)-1:
                    seq_count += 1
                print("next miss",next_count)
            if self.miss_count == 1:
                print('next is same')
                if seq_count < len(self.cent_lst)-1:
                    seq_count += 1
            
            if self.miss_count > 2:
                return
            self.next_cent(seq_count, next_count)

	
#lst = [[848, 301], [896, 213], [989, 375]]     
#lst = [[115, 449], [190, 452], [268, 451], [311, 451], [388, 454], [441, 451], [491, 448], [538, 445], [575, 443], [609, 424], [677, 424], [729, 443], [806, 443], [869, 441], [940, 447], [998, 450], [1067, 445]]
#[[791, 281], [865, 574], [881, 322], [1020, ], [1191, 459]]
#[[790, 284], [895, 215], [909, 326], [1023, 382], [1165, 455]]
#[[801, 287], [894, 214], [926, 342], [968, 202], [1025, 381], [1120, 432], [1168, 457]]
#c = Detect()
#c.key_values(lst)
#[[744, 280], [757, 148], [802, 158], [829, 287], [928, 392], [1028, 379], [1097, 423], [1157, 453], [1251, 423]]
#[[768, 283], [771, 156], [842, 294], [927, 350], [954, 424], [1037, 376], [1100, 423], [1156, 451], [1247, 431]]
