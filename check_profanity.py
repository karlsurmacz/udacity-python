# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 06:21:50 2016

@author: karl.surmacz
"""

import urllib

def read_text(file_name):
    quotes = open(file_name)
    contents = quotes.read()
    #print(contents)
    quotes.close
    check_profanity(contents)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity alert!!")
    elif "false" in output:
        print("No profanity")
    else:
        print("Could not scan")
    
if __name__ == "__main__":
    read_text("C:\Users\karl.surmacz\MAT\src\udacity-python\guardian_text.txt")