# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 09:28:27 2016

@author: karl.surmacz
"""

import os
import numpy as np
from shutil import copyfile

def secret_message():
    file_list = os.listdir(r"C:\Users\karl.surmacz\MAT\src\training\python-refresher\alphabet")
    print(file_list)
    os.chdir(r"C:\Users\karl.surmacz\MAT\src\training\python-refresher\alphabet")    
    
    # create a new directory for message if it doesn't exist
    new_path = r"C:\Users\karl.surmacz\MAT\src\training\python-refresher\message"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        
    # Create array of integers spelling out message
    int_array = np.array([8, 5, 12, 12, 15, 28, 23, 15, 18, 12, 4, 27])
    int_count = 1
    for index in int_array:
        copyfile(file_list[index], new_path+"\\"+str(int_count)+file_list[index])
        int_count+=1
        
secret_message()