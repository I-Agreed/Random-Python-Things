import turtle
from tkinter import *
import time
root = Tk()
turtle.tracer(0,0)
turtle.ht()
turtle.speed(50000000)
size = 1
a = Entry(root)
a.pack()
time.sleep(1)
def start(e=None):
    turtle.home()
    global a
    global b
    b = 0
    while b < 1:
        turtle.clear()
        #size += 1
        a.get()
        if a.get() != "":
            size = int(a.get())
            c = 0
            while c < size:
                c += 1
                turtle.forward(750/size)
                turtle.left(360/size)
            turtle.update()
            #time.sleep(0.1)
        b += 1

root.bind('<Return>',start)
root.mainloop()
