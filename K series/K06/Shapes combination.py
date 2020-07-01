import turtle
import random
def polygon(n,size,color):
    t.pencolor('hot pink')
    t.fillcolor(color)
    t.begin_fill()
    if n == 2:
        t.circle(size)
    else:
        
        t.left(random.randint(0,360)) #Rotate shapes into random direction
        for i in range(n):
            t.lt(360/n)
            t.forward(size)
    t.end_fill()
    
##Initialize
r0 = 1000
bg = input("Please enter background colour(name/colour code):") #Default = white
colors  = ["dark magenta","dark violet","dark orchid","medium orchid","purple","deep pink","magenta"]
turtle.setworldcoordinates(-r0,-r0,r0,r0)
t = turtle.Turtle()
t.pencolor('pink')

##Background
t.fillcolor(bg)
t.pu()
r = 1050
t.goto(-r,-r)
t.begin_fill()
t.pd()
t.goto(r,-r)
t.goto(r,r)
t.goto(-r,r)
t.goto(-r,-r)
t.end_fill()

##Draw Shapes
turtle.tracer(0)
for i in range(150):
    p1 = random.randint(1,1000)
    p2 = random.randint(1,1000)
    x = -r0 + r0 * p1 / 1000 * 2 #Normalize the position of shapes
    y = -r0 + r0 * p2 / 1000 * 2
    p3 = random.randint(1,100)
    t.penup()
    t.goto(x,y)
    t.pendown()
    c = random.choice(colors)
    #Reduce amount of large shapes
    if p3 < 95:
        polygon(random.randint(2,5),random.randint(50,90),c)
    else:
        polygon(random.randint(2,5),random.randint(110,130),c)
turtle.update()

    
        
