# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 18:11:21 2016

@author: karl.surmacz
"""

import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(100)
    for i in range(1,37):    
        draw_square(brad)
        brad.right(10)
        
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.circle(100)  

    window.exitonclick()

def draw_square(some_turtle):
    
    for iside in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)  
    
if __name__ == "__main__":
    draw_art()