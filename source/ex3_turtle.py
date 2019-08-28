from turtle import Turtle
import random

tina = Turtle()

def draw_circle(t_name, r,col,xcor=0,ycor=0):
    t_name.pu()
    t_name.color(col)
    t_name.dot(r*2)
    t_name.goto(xcor,ycor)

def random_radius():
    radius = [2,3,5,7,11,13,17,19,23,29]
    n = random.choice(radius)
    r = n * 17 / 3
    return r

#draw_circle(tina, 150,"blue",50,0)
#draw_circle(tina, 100,"red",0,50)
#draw_circle(tina, 50, "yellow",50,0)

colors = ['blue','red','yellow','green','purple','brown']

draw_circle(tina,random_radius(),random.choice(colors),random_radius(),random_radius())
draw_circle(tina,random_radius(),random.choice(colors),random_radius(),random_radius())
