# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:28:57 2019

@author: Darshit.Purohit
"""
import yolo
#
#def frame_creator(path, maxpeople):
#    maxpeople = maxpeople
#    import cv2
#    # Opens the Video file
#    cap= cv2.VideoCapture(path)
#    i=0
#    j=0
#    
#    while(cap.isOpened()):
#        ret, frame = cap.read()
#        if ret == True:
#            
#            if path == 0:
#                get_image(frame,j, maxpeople)
#            else :
#                 if i%100 == 0:
##                    ims = cv2.resize(frame, (800, 600))
##                    frame = frame[172:653, 48:211] # test3
##                    frame = frame [217:566, 724:1280] #test2
##                    frame = frame[3:697, 306:654] #video1
##                    frame = frame[371:1070, 12:1376] #youtube
#                    cv2.imwrite('Output/frame'+str(j)+'.jpg',frame)
#                    get_image(frame,j, maxpeople)
#           
#            j+=1
#            
##            if j > 100:
##                j=0
#            i+=1
#    
#        else:
#            break
#        
#    cap.release()
#    cv2.destroyAllWindows()
#
def frame_creator(path, maxpeople):
    maxpeople = maxpeople
    import cv2
    img = cv2.imread(path)
#    img = img[0:349, 272:556]
    cv2.imwrite('Output/frame1.jpg',img)
    get_image(img,3,maxpeople)    
#    
    
    
def get_image(fname, frame_no, maxpeople):
    img_name = fname
    frame_no =  frame_no
    maxpeople = maxpeople
    yolo.count_person(img_name, frame_no, maxpeople)