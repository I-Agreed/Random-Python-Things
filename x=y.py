import turtle
import math
turtle.speed(500)
turtle.delay(0.1)
turtle.ht()
turtle.penup()
turtle.setx(-600)
turtle.pendown()
turtle2 = turtle.clone()
turtle2.ht()
turtle2.pencolor("white")
turtle2.penup()
turtle2.forward(3)
turtle2.pendown()
repeat = 0
while 1==1:
    turtle.forward(1)
    turtle.sety(math.tan(math.tan(turtle.xcor())))
    turtle2.forward(1)
    turtle2.sety(math.tan(math.tan(turtle2.xcor())))
    if turtle.xcor() >599:
        turtle.penup()
        turtle.forward(-1200)
        turtle.pendown()
        turtle.forward(0.1)
        clear = 1
    if turtle2.xcor() > 599:
        if repeat == 1:
            turtle2.penup()
            turtle2.forward(-1200)
            turtle2.pendown()
            turtle2.forward(0.1)
        else:
            turtle2.penup()
            turtle2.forward(-1200)
            turtle2.pendown()
            repeat = 1
    
