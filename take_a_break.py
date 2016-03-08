# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 08:43:34 2016

@author: karl.surmacz
"""
import webbrowser
import time

total_breaks = 3
wait_time = 10
print("This program started on "+time.ctime())
for ibreak in range (0, total_breaks):
    time.sleep(wait_time)
    webbrowser.open("https://www.youtube.com/watch?v=StTqXEQ2l-Y")