# playing with rectangles
from turtle import Turtle

# Define a function to draw rectangles
def draw_rectangle(t_name,long,short,color,xcor=0,ycor=0):
    '''
    this is a function to draw rectangles by getting the long and short sides of it.
    Parameters:
    turtle name
    long side size
    short side size
    color of the rectangle
    x coordinate for the turtle to start (default 0)
    y coordinate for the turtle to start (default 0)
    '''
    t_name.color(color)
    t_name.penup()
    t_name.setposition(xcor,ycor)
    t_name.pendown()

    for i in range(2):
        t_name.forward(long)
        t_name.left(90)
        t_name.forward(short)
        t_name.left(90)


# we now define properties of the rectangles.
def area_rectangle(long,short):
    return long * short

def perimeter_rectangle():
    return (2*long)+(2*sort)


# Our turtle
linda = Turtle()
draw_rectangle(linda,100,30,'red')
linda.write("Area: " + str(area_rectangle(100,30)), align="left")


# we draw 18 rectangles and slightly rotate them. We can create beautiful figures like this.
longside = 50
shortside = 20
x1 = -150
y1= -150
for i in range(18):
    draw_rectangle(linda,longside,shortside,'purple',x1,y1)
    linda.right(20)
