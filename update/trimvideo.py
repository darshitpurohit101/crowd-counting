# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:35:51 2019

@author: Darshit.Purohit
"""


from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
x = 4000
y = 7000 

ffmpeg_extract_subclip("Dataset/CAFETERIA2.mp4",x, y, targetname="Dataset/testFinal1.mp4")
    