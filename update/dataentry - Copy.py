# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:24:45 2020

@author: Darshit.Purohit
"""
from csv import writer

def datawrite(testcase, count):
 
    with open('QueueDetectTesting.csv', 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([testcase, count])