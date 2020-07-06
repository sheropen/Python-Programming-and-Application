import turtle
def move(x,y):
    t.pu(),t.goto(x,y),t.pd()
def f(x,c):
    return x*x + c
turtle.setworldcoordinates(-2,-1.5,1,1.5)
turtle.tracer(0)
t = turtle.Turtle()
for i in range(-200,100):
    for j in range(-150,150):
        flag = True
        x = i / 100
        y = j / 100
        move(x,y)
        c = complex(x,y)
        z = complex(0)
        for j in range(100):
            z = f(z,c)
            if(abs(z)>2):
                flag = False
                break
        if(flag):
            t.dot(5,'black')
t.hideturtle()
turtle.update()
turtle.done()
