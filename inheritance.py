# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:51:57 2016

@author: karl.surmacz
"""

class Parent():
    def __init__(self, last_name, eye_colour):
        print("Parent constructor called")        
        self.last_name = last_name
        self.eye_colour = eye_colour
        
class Child(Parent):
    def __init__(self, last_name, eye_colour, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_colour)
        self.number_of_toys = number_of_toys
        
miley_cyrus = Child("Cyrus", "blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)