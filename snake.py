import turtle
import time
import random

turtle.speed(500)
turtle.tracer(0,0)
turtle.ht()
turtle.color("black")

# - - - - EDIT - - - - #
scale = 1

#default 0.1
frameDelay = 0.05
coolTail = True
tailColour = "white"
altTailColour = "black"
headColour = "black"
deathColour = "red"
altDeathColour = "#a30000"
foodColour = "blue"
wallColour = "green"
gridColour = "black"
backgroundColour = "white"

goodHead = False
circleSnake = True

circleFood = True

gridSizeX = 40
gridSizeY = 40
gridOn = False

startingX = 0
startingY = 0
startingDirection = "right"

displayScore = True

centerMap = True
homeDot = False

cheatEnabled = True

foodQuantity = 5

startingLength = 3

goodTime = True

wall = False
# if not then the snake loops around

# - - - - DONT EDIT - - - - #
turtle.bgcolor(backgroundColour)
started = 0
if centerMap:
    offsetX = int((gridSizeX*scale*10)/2)
    offsetY = int((gridSizeY*scale*10)/2)
else:
    offsetX = 0
    offsetY = 0
cheat = False
gridXSize = gridSizeX - 1
gridYSize = gridSizeY - 1
hasMoved = False
addTail = False
foodX = -5
foodY = -5
foodCoords = set()

if centerMap:
    if wall:
        turtle.screensize(gridSizeX*scale*10+20*scale,gridSizeY*scale*10+20*scale)
    else:
        turtle.screensize(gridSizeX*scale*10,gridSizeY*scale*10)

def getGridString(num):
    a = str()
    for i in range(0,num):
        if not i + 1 == num:
            a = a + "a"
        else:
            a = a + "b"
    return a

def grid():
    a = turtle.color()
    turtle.color(gridColour)
    turtle.penup()
    turtle.goto(0-offsetX,0-offsetY)
    turtle.pendown()
    for h in getGridString(gridSizeY):
        turtle.forward(10*scale)
        turtle.left(90)
        for i in getGridString(gridSizeX):
            
            if i == "a":
                
                for j in "aaa":
                    turtle.forward(10*scale)
                    turtle.left(90)
                turtle.forward(20*scale)
                turtle.left(90)

            elif i =="b":
                for j in "aaa":
                    turtle.forward(10*scale)
                    turtle.left(90)
                turtle.setx(0-offsetX)
                turtle.sety(turtle.ycor() + 10*scale)
    if homeDot:
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.dot(5*scale)
        
def dotColour(x,y,shade="black",outline=False):
    if shade == backgroundColour:
        outline = True
    a = turtle.color()[0]
    turtle.color(shade)
    turtle.penup()
    turtle.goto((x*10*scale)-offsetX+5*scale,(y*10*scale)-offsetY)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5*scale)
    turtle.end_fill()
    if outline:
        turtle.color("black")
        turtle.circle(5*scale)
    turtle.color(a)
    
def circleColour(x,y,shade="black",outline=False):
    if shade == backgroundColour:
        outline = True
    a = turtle.color()[0]
    turtle.color(shade)
    turtle.penup()
    turtle.goto((x*10*scale)-offsetX+5*scale,(y*10*scale)-offsetY)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5*scale)
    if snek.direction == "left":
        pass
    elif snek.direction == "right":
        turtle.goto((x*10*scale)-offsetX,(y*10*scale)-offsetY)
    elif snek.direction == "up":
        turtle.goto((x*10*scale)-offsetX*scale,(y*10*scale)-offsetY)
    elif snek.direction == "down":
        turtle.goto((x*10*scale)-offsetX*scale,(y*10*scale)-offsetY+5*scale)
    if snek.direction == "left" or snek.direction == "right":
        for i in "aa":
            turtle.forward(5*scale)
            turtle.left(90)
            turtle.forward(10*scale)
            turtle.left(90)
    elif snek.direction == "up" or snek.direction == "down":
        for i in "aa":
            turtle.forward(10*scale)
            turtle.left(90)
            turtle.forward(5*scale)
            turtle.left(90)
    turtle.end_fill()
    if outline and gridOn:
        turtle.color("black")
        for i in "aaaa":
            turtle.forward(10*scale)
            turtle.left(90)
    turtle.color(a)

def colour(x,y,shade="black",outline=False):
    if shade == backgroundColour:
        outline = True
    a = turtle.color()[0]
    turtle.color(shade)
    turtle.penup()
    turtle.goto((x*10*scale)-offsetX,(y*10*scale)-offsetY)
    turtle.pendown()
    turtle.begin_fill()
    for i in "aaaa":
        turtle.forward(10*scale)
        turtle.left(90)
    turtle.end_fill()
    if outline and gridOn:
        turtle.color("black")
        for i in "aaaa":
            turtle.forward(10*scale)
            turtle.left(90)
    turtle.color(a)
    

class snake:
    def __init__(self,x,y,direction):
        self.len = 0
        self.x = x
        self.y = y
        self.direction = direction
        self.tails = list()
        self.dead = False
        
    def getCoords(self):
        return (self.x,self.y)
    
    def forward(self):
        if self.direction  == "up":
            self.y += 1
            
        elif self.direction  == "down":
            self.y -= 1

        elif self.direction  == "left":
            self.x -= 1

        elif self.direction  == "right":
            self.x += 1
            
    def backward(self):
        if self.direction  == "up":
            self.y -= 1
            
        elif self.direction  == "down":
            self.y += 1

        elif self.direction  == "left":
            self.x += 1

        elif self.direction  == "right":
            self.x -= 1
            
    def setDirection(self,direction):
        self.direction = direction
    
    def tailGen(self):
        if not self.tails.__len__() < 1:
            if not addTail:
                self.tails.pop(self.tails.__len__() - 1)
            self.tails.insert(0,(self.x,self.y))

        elif addTail:
            self.tails.insert(0,(self.x,self.y))
            
def drawTail(shade="black",altShade="black"):
    if coolTail:
        a = True
        for i in snek.tails:
            if a:
                if circleSnake:
                    dotColour(i[0],i[1],shade)
                    a = not(a)
                else:
                    colour(i[0],i[1],shade)
                    a = not(a)
            else:
                if circleSnake:
                    dotColour(i[0],i[1],altShade)
                    a = not(a)
                else:
                    colour(i[0],i[1],altShade)
                    a = not(a)
    else:     
        for i in snek.tails:
            if circleSnake:
                dotColour(i[0],i[1],shade)
                a = not(a)
            else:
                colour(i[0],i[1],shade)
                a = not(a)

def checkDeath():
    if wall:
        if snek.x < 0 or snek.x > gridXSize or snek.y < 0 or snek.y > gridYSize or snek.tails.__contains__((snek.x,snek.y)):
            if circleSnake:
                dotColour(snek.x,snek.y,deathColour,True)
            else:
                colour(snek.x,snek.y,deathColour,True)
            snek.dead = True
            drawTail(deathColour,altDeathColour)
    else:
        if snek.tails.__contains__((snek.x,snek.y)):
            if circleSnake:
                dotColour(snek.x,snek.y,deathColour,True)
            else:
                colour(snek.x,snek.y,deathColour,True)
            snek.dead = True
            drawTail(deathColour,altDeathColour)
            
        if snek.x < 0:
            snek.x = gridXSize
            checkFood()

        if snek.x > gridXSize:
            snek.x = 0
            checkFood()

        if snek.y < 0:
            snek.y = gridYSize
            checkFood()

        if snek.y > gridYSize:
            snek.y = 0
            checkFood()
        
def left():
    global hasMoved
    if not snek.direction == "right" and not hasMoved:
        snek.setDirection("left")
        hasMoved = True

def score():
    if displayScore:
        turtle.title("Snake Game - Score: {}".format(snek.tails.__len__()))
   
def right():
    global hasMoved
    if not snek.direction == "left" and not hasMoved:
        snek.setDirection("right")
        hasMoved = True

def up():
    global hasMoved
    if not snek.direction == "down" and not hasMoved:
        snek.setDirection("up")
        hasMoved = True

def down():
    global hasMoved
    if not snek.direction == "up" and not hasMoved:
        snek.setDirection("down")
        hasMoved = True
        
def tailAdd():
    global addTail
    addTail = True

def addFood():
    global foodX
    global foodY
    if not foodCoords.__len__() > foodQuantity + 1:
        x = random.randint(0,gridXSize)
        y = random.randint(0,gridYSize)
        if circleFood:
            dotColour(x,y,foodColour)
        else:
            colour(x,y,foodColour)
        foodCoords.add((x,y))

def checkFood():
    global addTail
    for i in foodCoords:
        if circleFood:
            dotColour(i[0],i[1],foodColour)
        else:
            colour(i[0],i[1],foodColour)
    if foodCoords.__contains__((snek.x,snek.y)):
        foodCoords.remove((snek.x,snek.y))
        addTail = True
        addFood()

def start():
    global started
    if started < startingLength - 1:
        snek.tails.append((snek.x,snek.y))
        started += 1

def drawSnek():
    if goodHead:
        if not snek.dead:
            circleColour(snek.x,snek.y,headColour)
    elif circleSnake:
        if not snek.dead:
            dotColour(snek.x,snek.y,headColour)
    else:
        if not snek.dead:
            colour(snek.x,snek.y,headColour)

def frame():
    if goodTime:
        if not frameDelay - (time.time() - startTime) < 0:
            time.sleep(frameDelay - (time.time() - startTime))
        else:
            pass
    else:
        time.sleep(frameDelay)

def walls():
    if wall:
        for i in range(0,gridSizeX+2):
            colour(i-1,-1,wallColour,True)
            
        for i in range(0,gridSizeX+2):
            colour(i-1,gridSizeY,wallColour,True)

        for i in range(0,gridSizeY):
            colour(-1,i,wallColour,True)

        for i in range(0,gridSizeY):
            colour(gridSizeX,i,wallColour,True)

def cheatCode():
    global cheat
    cheat = True
    
def reset():
    global addTail
    global hasMoved
    global cheat
    hasMoved = False
    if not cheat:
        addTail = False
    if cheat:
        addTail = True
        cheat = False
        
def border():
    turtle.penup()
    turtle.goto(0-offsetX,0-offsetY)
    turtle.pendown()
    turtle.forward(10*scale*(gridXSize+1))
    turtle.left(90)
    turtle.forward(10*scale*(gridYSize+1))
    turtle.left(90)
    turtle.forward(10*scale*(gridXSize+1))
    turtle.left(90)
    turtle.forward(10*scale*(gridYSize+1))
    turtle.left(90)
snek = snake(startingX,startingY,startingDirection)

turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
if cheatEnabled:
    turtle.onkey(cheatCode,"q")

turtle.listen()
for i in range(0,foodQuantity):
    addFood()
while not snek.dead:
    turtle.clear()
    startTime = time.time()
    reset()
    walls()
    start()
    snek.forward()
    checkFood()
    drawTail(tailColour,altTailColour)
    score()
    checkDeath()
    drawSnek()
    snek.tailGen()
    if gridOn:
        grid()
    else:
        border()
    turtle.update()
    frame()
