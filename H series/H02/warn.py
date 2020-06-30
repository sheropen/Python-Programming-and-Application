#Warning Signboard
import turtle
import math
    
n = int(input())
t = turtle.Turtle()
t.pencolor("black")
t.pensize(3)

##Triangle Outside
t.fillcolor("black")
t.begin_fill()
t.forward(n/2)
r = n*0.03 #Radius to soften edge

t.circle(r,120)
t.forward(n)
t.circle(r,120)
t.forward(n)
t.circle(r,120)
t.forward(n/2)
t.end_fill()

##Triangle Inside
t.left(90)
t.forward(n*(1-(math.sqrt(3)/2))/2.5)
t.right(90)
n*= 0.9
t.fillcolor("yellow")
t.begin_fill()
t.forward(n/2)
t.left(120)
t.forward(n)
t.left(120)
t.forward(n)
t.left(120)
t.forward(n/2)
t.end_fill()

## "!"
#Bottom Part
t.left(90)
t.pu()
t.forward(n*0.1)
r = n*0.05
t.right(90)
t.pd()
t.fillcolor("black")
t.begin_fill()
t.circle(r)
t.end_fill()

#Upper Part
t.pu()
t.left(90)
t.forward(r*3)
t.pd()
t.begin_fill()
t.right(10)
l = n * 0.3
t.forward(l)
t.left(100)
t.forward(l*math.sin(math.radians(10))*2)
t.left(100)
t.forward(l)
t.end_fill()

t.pu()
t.left(170)
t.forward(l*math.cos(math.radians(10)))
t.right(90)
t.forward(l*math.sin(math.radians(10)))
t.left(90)
t.pd()
t.begin_fill()
t.circle(l*math.sin(math.radians(10)),180)
t.left(90)
t.forward(l*math.sin(math.radians(10))*2)
t.end_fill()






