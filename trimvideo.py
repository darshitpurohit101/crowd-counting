# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:35:51 2019

@author: Darshit.Purohit
"""


from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
x = 6360
y = 6540

for i in range(7,10):
    ffmpeg_extract_subclip("Dataset/CAFETERIA3.mp4",x, y, targetname="Dataset/test3-{}".format(i)+".mp4")
    x = y
    y += 180
    