# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:28:57 2019

@author: Darshit.Purohit
"""
import yolo
import divide
import Roi_selection
import csv
#import crop2
import draw
import cv2
#
#def frame_creator(path, maxpeople,r):
#    maxpeople = maxpeople
#    
#    # Opens the Video file
#    cap= cv2.VideoCapture(path)
#    i=0
#    j=0
##    ret, frame = cap.read()
#    while(cap.isOpened()):
#        ret, frame = cap.read()
#        if ret == True:
#            
##            cv2.imwrite('Output/test.jpg',frame)
#            if path == 0:
#                get_image(frame,j, maxpeople)
#            else :
#                 if i%5 == 0:
#                         get_image( frame, j, maxpeople, i,r)
#                         cv2.imwrite('Input/input'+str(j)+'.jpg',frame)
#                         j+=1
##                    ims = cv2.resize(frame, (800, 600))
##                    frame = frame[172:653, 48:211] # test3
##                    cv2.imwrite('first.jpg',frame)
##                    frame = frame [37:694, 591:1280] #test2
##                    frame = frame[3:697, 306:654] #video1
##                    frame = frame[371:1070, 12:1376] #youtube
##                    cv2.imwrite('second.jpg',frame)
##                    frame = Roi_selection.roi(frame)
##                    cv2.imwrite('third.jpg',frame)
##                    cv2.imwrite('Output/test2.jpg',frame)
##                    frame = frame[228:574, 165:762] # for ROI
##                    frame = frame[219:531, 192:727] # Dont touch this......
##                    frame = frame[247:596, 157:735] # 99%
##                    cv2.imwrite('fourth.jpg', frame)
##                    frame = frame[38:297, 3:535]
##                    cv2.imwrite('fifth.jpg',frame)
##                    cv2.imwrite('Output/test3.jpg',frame)
##                    imCrop1, imCrop2 = divide.divide(frame)
#                    
##                    cv2.imwrite('Output/crop1.jpg', imCrop1) #store crop1
##                    cv2.imwrite('Output/crop2.jpg',imCrop2) #store crop2
##                    cv2.imwrite('Output/input{}.jpg'.format(j),frame)
##                    for i in range(1,3):
##                        name = 'imCrop{}'.format(i)
##                        print(name)
##                        im = vars()[name]
##                        get_image( im, j, maxpeople, i)
#                       
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
def frame_creator(path, maxpeople,r):
    maxpeople = maxpeople
#    import cv2
    img = cv2.imread(path)
#    t = crop2.cordinates()
#    r = t.cord(img)
#    img = img[0:349, 272:556]
#    cv2.imwrite('Output/frame1.jpg',frame)
    get_image(img,3,maxpeople,1,r)    
#####    
    
    
def get_image(fname, frame_no, maxpeople, i,r):
    img_name = fname
    i = i
    frame_no =  frame_no
    maxpeople = maxpeople
    yolo.count_person(img_name, frame_no, maxpeople, i,r)