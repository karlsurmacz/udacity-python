# -*- coding: utf-8 *-
"""
Created on Mon Mar 07 18:49:54 2016

@author: karl.surmacz
"""

import turtle

def draw_fractal():
    window = turtle.Screen()
    window.bgcolor("red")    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.fillcolor("green")
    brad.speed(100)
    draw_triangle_trio_trio(brad)
    window.exitonclick()
    
def new_triangle_left(angle, length, some_turtle):
    some_turtle.penup()
    some_turtle.left(angle)
    some_turtle.forward(length)
    some_turtle.right(angle)
    some_turtle.pendown()
    
def new_triangle_right(angle, length, some_turtle):
    some_turtle.penup()
    some_turtle.right(angle)
    some_turtle.forward(length)
    some_turtle.left(angle)
    some_turtle.pendown()
    
def draw_triangle_trio_trio(some_turtle):

    some_turtle.fill(True)    
    draw_triangle_trio(some_turtle)
    some_turtle.fill(False)  
    new_triangle_left(60, 200, some_turtle)
    
    some_turtle.fill(True)    
    draw_triangle_trio(some_turtle)
    some_turtle.fill(False)  
    new_triangle_right(60, 200, some_turtle)
    
    some_turtle.fill(True)    
    draw_triangle_trio(some_turtle)
    some_turtle.fill(False)  
        
    some_turtle.home()  
    
def draw_triangle_trio(some_turtle):
        
    some_turtle.fill(True)    
    draw_triangle(some_turtle)
    some_turtle.fill(False)  
    new_triangle_left(60, 100, some_turtle)
    
    some_turtle.fill(True)    
    draw_triangle(some_turtle)
    some_turtle.fill(False)  
    new_triangle_right(60, 100, some_turtle)
    
    some_turtle.fill(True)    
    draw_triangle(some_turtle)
    some_turtle.fill(False)  
    
    some_turtle.penup()    
    some_turtle.right(180) 
    some_turtle.forward(100)
    some_turtle.left(180) 
    some_turtle.pendown()
    
def draw_triangle(some_turtle):
    for i in range(0,3):    
        some_turtle.forward(100)
        some_turtle.left(120)
    
if __name__ == "__main__":
    draw_fractal()