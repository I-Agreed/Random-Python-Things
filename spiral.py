import turtle
import hd
steps = 50
numbers = list()
turtle.speed(100)
turtle.ht()
turtle.tracer(0,0)

def genfib():
    global numbers
    a = 0
    numbers.append(1)
    numbers.append(1)
    while a < steps:
        a += 1
        b = numbers.__len__()
        c = b - 1
        d = b - 2
        numbers.append(numbers[c] + numbers[d])

def genspiral():
    global steps
    global numbers
    a = -1
    turtle.left(90)
    while a < (steps - 1):
        a += 1
        turtle.circle(numbers[a],9)

def genspiralwsquare():
    global steps
    global numbers
    a = -1
    turtle.left(90)
    while a < (steps - 1):
        a += 1
        for i in "aaaa":
            turtle.forward(numbers[a])
            turtle.left(90)
        turtle.circle(numbers[a],90)
        
genfib()
genspiralwsquare()
turtle.update
