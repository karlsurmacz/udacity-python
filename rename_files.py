# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 09:05:16 2016

@author: karl.surmacz
"""
import os
def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Users\karl.surmacz\MAT\src\training\python-refresher\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\karl.surmacz\MAT\src\training\python-refresher\prank")
    
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        
    os.chdir = saved_path
rename_files()