# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:27:31 2019

@author: Darshit.Purohit
"""

import tkinter
global root
def up(a):
    root = tkinter.Tk()
    vr = tkinter.StringVar()
    vr.set(a)
    t = tkinter.Label(root, textvariable=vr)
    t.pack()
    root.mainloop()
    return None    