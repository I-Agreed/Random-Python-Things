import turtle
import time
import random
turtle.tracer(0,0)



frameDelay = 0.05
resistance = 1

timer = 60

maxX = 300
maxY = 300
colour = "#44ff51"
turtle.bgcolor("black")

ships = set()
deadShips = set()
newShips= set()
def drawBox():
    a = turtle.Turtle()
    a.color(colour)
    a.ht()
    a.speed(500)
    a.penup()
    a.goto(maxX,maxY)
    a.pendown()
    a.goto(maxX,-maxY)
    a.goto(-maxX,-maxY)
    a.goto(-maxX,maxY)
    a.goto(maxX,maxY)
    
class ship(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.color(colour)
        
        self.penup()
        self.speed(500)

        self.shootDelay = 10
        self.delay = 0

        ships.add(self)
        self.shapesize(stretch_len=2,stretch_wid=1.5)

        self.handle = 3
        self.max = 20
        self.maxBack = 10
        self.speed = 0
        self.angSpeed = 0
        self.angMax = 10
        self.accel = 1
        
        self.b = False
        self.f = False
        self.l = False
        self.r = False

        self.handled = False
        self.acceled = False

        self.shots = set()
        self.newShots = set()
        self.deadShots = set()

    def shoot(self):
        if self.delay <= 0:
            self.newShots.add(shot(self))
            self.delay = self.shootDelay
        
    def moveLeft(self):
        if not self.angSpeed - self.handle < self.angMax*-1:
            self.angSpeed -= self.handle
        else:
            self.angSpeed = self.angMax*-1
        self.handled = True

    def moveRight(self):
        if not self.angSpeed + self.handle > self.angMax:
            self.angSpeed += self.handle
        else:
            self.angSpeed = self.angMax
        self.handled = True

    def move(self,e=1):
        if not self.speed + self.accel >= self.max:
            self.speed += self.accel
        else:
            self.speed = self.max
        self.acceled = True

    def moveBack(self,e=1):
        if not self.speed - self.accel <= -self.maxBack:
            self.speed -= self.accel
        else:
            self.speed = -self.maxBack
        self.acceled = True

    def update(self):
        if self.f:
            self.move()
        if self.b:
            self.moveBack()
        if self.l:
            self.moveLeft()
        if self.r:
            self.moveRight()

        
        if not self.acceled:
            if self.speed > 0:
                if self.speed < resistance:
                    self.speed = 0
                else:
                    self.speed -= resistance

            elif self.speed < 0:
                if self.speed > -resistance:
                    self.speed = 0
                else:
                    self.speed += resistance

        if not self.handled:
            if self.angSpeed < resistance:
                self.angSpeed = 0
            else:
                self.angSpeed -= resistance



        self.right(self.angSpeed)
        self.forward(self.speed)

        self.handled = False
        self.acceled = False

        if self.xcor() > maxX:
            self.setx(-maxX)
        if self.xcor() < -maxX:
            self.setx(maxX)

        if self.ycor() > maxY:
            self.sety(-maxY)
        if self.ycor() < -maxY:
            self.sety(maxY)

        for i in self.shots:
            i.update()
            
        for i in self.deadShots:
            self.shots.remove(i)

        for i in self.newShots:
            self.shots.add(i)
            
        self.deadShots = set()
        self.newShots = set()

        self.delay -= 1

class shot(turtle.Turtle):
    def __init__(self,parent):
        turtle.Turtle.__init__(self)
        self.shape("shot")
        self.parent = parent
        self.color(colour)
        self.speed(500)
        self.moveSpeed = 10 + parent.speed
        self.seth(parent.heading())
        self.penup()
        self.goto(*parent.pos())
        self.shapesize(0.5)
        self.shapesize(outline=2)
        self.life = 20

        self.children = set()

    def update(self):
        self.forward(self.moveSpeed)
        self.life -= 1
        if self.life < 0:
            self.ht()
            self.parent.deadShots.add(self)
            self.__del__()

        if self.xcor() > maxX:
            self.setx(-maxX)
        if self.xcor() < -maxX:
            self.setx(maxX)

        if self.ycor() > maxY:
            self.sety(-maxY)
        if self.ycor() < -maxY:
            self.sety(maxY)

    def delete(self):
        self.ht()
        self.parent.deadShots.add(self)
        self.__del__()

    def __del__(self):
        for i in range(6):
            self.parent.newShots.add(explode(self.xcor(),self.ycor(),self.parent))

class explode(turtle.Turtle):
    def __init__(self,x,y,parent):
        turtle.Turtle.__init__(self)
        self.color(colour)
        self.shape("circle")
        self.life = 4
        self.parent = parent
        self.penup()
        self.moveSpeed = 5
        self.goto(x,y)
        self.seth(random.randint(0,360))
        self.speed(500)
        self.shapesize(0.1)

    def update(self):
        self.forward(self.moveSpeed)

        if self.moveSpeed < resistance:
            self.speed = 0
        else:
            self.moveSpeed -= resistance

        self.life -= 1
        if self.life < 0:
            self.ht()
            self.parent.deadShots.add(self)

        if self.xcor() > maxX:
            self.setx(-maxX)
        if self.xcor() < -maxX:
            self.setx(maxX)

        if self.ycor() > maxY:
            self.sety(-maxY)
        if self.ycor() < -maxY:
            self.sety(maxY)

class enemy(turtle.Turtle):
    def __init__(self,x=0,y=0):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        newShips.add(self)
        self.shape("circle")
        self.color(colour)
        self.penup()
        self.hit = 10

    def update(self):
        for i in ships:
            if type(i) == ship:
                for j in i.shots:
                    if type(j) == shot:

                        if j.xcor() >= self.xcor()-self.hit and \
                            j.xcor() <= self.xcor()+self.hit and \
                            j.ycor() >= self.ycor()-self.hit and \
                            j.ycor() <= self.ycor()+self.hit:
                            j.delete()
                            self.delete()

    def delete(self):
        global score
        score += 1
        deadShips.add(self)
        self.ht()
        newShips.add(enemy(random.randint(-maxX,maxX),random.randint(-maxY,maxY)))
        

    
                        
    
def playerStartMove():
    turtle.onkeyrelease(playerStopMove,"w")
    player.f = True

def playerStopMove():
    turtle.onkeypress(playerStartMove,"w")
    player.f = False

def playerStartBack():
    turtle.onkeyrelease(playerStopBack,"s")
    player.b = True

def playerStopBack():
    turtle.onkeypress(playerStartBack,"s")
    player.b = False

def playerStartLeft():
    turtle.onkeyrelease(playerStopLeft,"a")
    player.l = True

def playerStopLeft():
    turtle.onkeypress(playerStartLeft,"a")
    player.l = False

def playerStartRight():
    turtle.onkeyrelease(playerStopRight,"d")
    player.r = True

def playerStopRight():
    turtle.onkeypress(playerStartRight,"d")
    player.r = False

def register():
    a = turtle.Turtle()
    a.ht()
    a.speed(500)

    a.width(2)
    a.color(colour)

    a.begin_poly()
    a.goto(-10,-5)
    a.goto(0,15)
    a.goto(10,-5)
    a.goto(0,0)
    a.end_poly()
    b = turtle.Shape("polygon",a.get_poly())
    turtle.register_shape("ship",b)

    a.begin_poly()
    a.penup()
    a.goto(0,5)
    a.pendown()
    a.goto(0,20)
    a.goto(0,5)
    a.penup()
    a.goto(0,0)
    a.pendown()
    a.end_poly()
    c = turtle.Shape("polygon",a.get_poly())
    turtle.register_shape("shot",c)

    a.begin_poly()
    a.penup()
    a.goto(0,-10)
    a.pendown()
    a.circle(10)
    a.penup()
    a.goto(0,0)
    a.pendown()
    a.end_poly()
    d = turtle.Shape("polygon",a.get_poly())
    turtle.register_shape("target",d)

    a.clear()
register()
writer = turtle.Turtle()
writer.color(colour)
writer.ht()
writer.penup()
writer.goto(-maxX+5,maxY-15)
writer.pendown()
def write(text):
    writer.clear()
    writer.write(text,font=('Consolas',8,'normal'))
    
player = ship()
turtle.onkeypress(playerStartMove,"w")
turtle.onkeypress(playerStartBack,"s")
turtle.onkeypress(playerStartLeft,"a")
turtle.onkeypress(playerStartRight,"d")
turtle.onkeypress(player.shoot,"space")
turtle.listen()

target = enemy()

drawBox()
score = 0
begin = time.time()
turtle.title("Game by Brendan")
while 1:
    write("Score: {0} Time Left: {1}".format(str(score),str(round(timer-(time.time()-begin),2))))
    if timer-(time.time()-begin) < 0:
        write("GAME OVER, Score: {0}".format(str(score)))
        break
    for i in ships:
        i.update()
    turtle.update()
    time.sleep(frameDelay)
    for i in deadShips:
        ships.remove(i)
    deadShips = set()
    for i in newShips:
        ships.add(i)
    newShips = set()
