# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:48:54 2019

@author: Darshit.Purohit
"""
#
#from tkinter import messagebox
#import tkinter
#root = tkinter.Tk()
#root.withdraw()
#
## message box display
#messagebox.showerror("Error", "Error message")
#messagebox.showwarning("Warning","Warning message")
#messagebox.showinfo("Information","Informative message")

import tkinter as tk
#import time

def alert(count):
    root = tk.Tk()
    root.title("Crowd Alert")
    alert_msg = "Place is too crowded.\n COUNT > "+ str(count)
    label = tk.Label(root, text=alert_msg)
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    button = tk.Button(root, text="OK", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    root.after(3000, lambda: root.destroy())
    root.mainloop()


#alert(3)
