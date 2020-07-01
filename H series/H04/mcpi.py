import turtle
import random
import math

##Initialize
t = turtle.Turtle()
turtle.setworldcoordinates(0,0,1,1)
turtle.tracer(0)
t.pensize(1)
t.pencolor('black')
t.pu()
t.goto(0,1)

##Draw 1/4 Circle
t.pd()
t.fillcolor('pale green')
t.begin_fill()
t.goto(0,0)
t.goto(1,0)
t.left(90)
t.circle(1,90,100)
t.end_fill()
res = 0

##Drop points
for i in range(20000):
    tx = random.uniform(0,1)
    ty = random.uniform(0,1)
    r = math.sqrt(tx*tx + ty*ty)
    t.pu()
    t.goto(tx,ty)
    t.pd()
    if(r <= 1):
        t.dot(2,'red')
        res += 1
    else:
        t.dot(2,'blue')
t.hideturtle()
turtle.update()

##Calculate Pi
print("Pi =",4*res/20000)

