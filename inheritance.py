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
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye colour - "+self.eye_colour)
        
class Child(Parent):
    def __init__(self, last_name, eye_colour, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_colour)
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye colour - "+self.eye_colour)
        print("# toys - "+str(self.number_of_toys))

       
billy_cyrus = Parent("Cyrus", "blue")       
miley_cyrus = Child("Cyrus", "blue", 5)
billy_cyrus.show_info()
miley_cyrus.show_info()