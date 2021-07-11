from turtle import *

def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

def teleport(x,y):
    penup()
    goto(x,y)
    pendown()

def circle(size):
    for i in range(360):
        forward(size)
        left(1)

def concentric_squares(size, x,y):
    teleport(x,y)
    square(size)
    teleport(x-size,x+size)
    square(size * 3)

concentric_squares(10,200,200)
teleport(0,0)
circle(1)

exitonclick()

