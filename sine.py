import turtle
import hd
import math
turtle.tracer(0,0)
turtle.ht()
turtle.delay(000)
turtle.width(1.5)

resolution = 13
scale = 6.5
increase = 1
textSize = 5
decimal = 2
text = False

xOffset = -100*scale
yOffset = -105*scale

def getH():
    a = (-turtle.heading()-270) % 360
    if a > 180:
        a -= 2*(a-180)
        a*= -1
    a = round(a,decimal)
    if a.is_integer():
        a = int(a)
    return str(a)


c = 0
while 1:
    turtle.seth(0)
    turtle.penup()
    turtle.goto(xOffset,yOffset)
    turtle.pendown()
    turtle.sety(-10*scale+yOffset)
    turtle.sety(0+yOffset)
    turtle.forward(200*scale)
    turtle.sety(-10*scale+yOffset)
    turtle.sety(0+yOffset)
    turtle.forward(-100*scale)
    turtle.penup()
    turtle.sety(110*scale+yOffset)
    turtle.pendown()
    a = 0


    turtle.seth(c)
    while a < resolution:
        turtle.left(360/resolution)
        a += 1
        
        turtle.forward(100*scale)
        turtle.penup()
        turtle.forward(10*scale)
        if text:
            turtle.write(getH(),align="center",font=('Arial',textSize,'normal'))
        if turtle.heading() == 270 and (90/(360/resolution)).is_integer():
            turtle.back(110*scale)
            turtle.pendown()
            continue
        turtle.back(10*scale)
        turtle.pendown()
        b = turtle.ycor()
        turtle.color("red")
        turtle.sety(10*scale+yOffset)
        turtle.penup()
        turtle.sety(0*scale+yOffset)
        turtle.color("black")
        turtle.pendown()
        turtle.sety(-10*scale+yOffset)
        turtle.penup()
        turtle.sety(-20*scale+yOffset)
        if text:
            turtle.write(round((turtle.xcor()-100*scale-xOffset)/(100*scale),decimal),align="center",font=('Arial',textSize,'normal'))

        turtle.sety(b)

        
        turtle.forward(-100*scale)
        turtle.pendown()
    turtle.penup()
    turtle.goto(0,10*scale+yOffset)
    turtle.pendown()
    turtle.seth(0)
    turtle.circle(100*scale,steps=100)
    turtle.update()
    if increase:

        c += increase
    else:
        turtle.done()
    turtle.clear()



