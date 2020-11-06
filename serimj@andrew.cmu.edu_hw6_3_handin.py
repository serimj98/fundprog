# Targets Game
# 15-112
# Name: Serim Jang
# Andrew ID: serimj

from tkinter import *
import random, math, copy

####################################
# customize these functions
####################################

# Initializes data
def init(data):
    data.width, data.height = 500, 500
    data.numCircles = 5
    data.radius = random.choice([5, 15, 25])
    data.choiceA = 5
    data.choiceB = 15
    data.choiceC = 25
    data.locationX = random.randint(0, data.width-(data.radius*2))
    data.locationY = random.randint(0, data.height-(data.radius*2))
    data.margin = 30
    data.numTargetPressed = 5

    # Starting screen begins by heading right/down
    data.headingRight = True
    data.headingDown = True

    # Adds onto the target location to bounce starting from a random point
    data.bounceStartX = data.locationX
    data.bounceStartY = data.locationY
    data.bounceEndX = data.radius*2 + data.locationX
    data.bounceEndY = data.radius*2 + data.locationY
    
    # Allows rectangle and object to move with the keyPressed function
    data.offset = 50
    data.offsetX = -250
    data.offsetY = -250
    data.offsetTargetX = 0
    data.offsetTargetY = 0

    # Keeps track of score and time left
    data.score = 0
    data.timeLeft = 20
    data.time = 0
    data.timerCounter = 0
    data.timeRadius = 500
    data.timeTimer = 1000
    data.timeEnd = 20000

    # Changes state of what stage the player is in the game
    data.gameStart = False
    data.drawStartingTarget = False
    data.gameOver = False

    # Finds the center of the target to create a list with random X, Y, radius
    data.centerX = random.randint((-data.width//2 + data.radius), \
                    ((data.width*3)//2 - data.radius))
    data.centerY = random.randint((-data.height//2 + data.radius), \
                    ((data.height*3)//2 - data.radius))
    data.list = [[data.centerX, data.centerY, data.radius]]
    
# Creates the starting screen before playing
def startingScreen(canvas, data):
    x0, y0 = 0, 0
    x1, y1 = data.width, data.height
    canvas.create_rectangle(x0, y0, x1, y1, fill = "SlateGray1")

# Displays text of game's name and instructions for starting
def startingText(canvas, data):
    canvas.create_text(data.width/2, data.height/3, text = "Targets Game!", \
    fill = "darkBlue", font = "Helvetica 40 bold")
    canvas.create_text(data.width/2, (data.height*3)/4, \
    text = "Press 'p' to play", fill = "darkBlue", font = "Helvetica 25")

# Draws target in the starting screen
def drawStartingTarget(canvas, data):
    for circle in range (data.numCircles): # alternating colors
        if circle % 2 == 0:  data.color = "red"
        if circle % 2 == 1:  data.color = "white"  
        x0 = data.radius*2*(circle/(2*data.numCircles)) + data.bounceStartX
        y0 = data.radius*2*(circle/(2*data.numCircles)) + data.bounceStartY
        x1 = data.radius*2*((2*data.numCircles)-circle)/(2*data.numCircles)+ \
                data.bounceStartX
        y1 = data.radius*2*((2*data.numCircles)-circle)/(2*data.numCircles)+\
                data.bounceStartY
        canvas.create_oval(x0, y0, x1, y1, fill = data.color, width = 0)

# Helper function to draw target in the game screen
def drawTarget(canvas,data):
    for circle in range(data.numCircles): # alternating colors
        if circle % 2 == 0: data.color = "red"
        elif circle % 2 == 1: data.color = "white"
        radius = data.radius - data.radius*circle/data.numCircles
        x0 = data.centerX - radius
        y0 = data.centerY - radius
        x1 = data.centerX + radius
        y1 = data.centerY + radius
        canvas.create_oval(x0 + data.offsetTargetX, y0 + data.offsetTargetY, \
                                x1+data.offsetTargetX, y1+data.offsetTargetY, \
                                fill = data.color, width = 0)
     
# Calls upon data.list to randomly place drawTarget in the rectangle boundaries
def drawGameTarget(canvas,data):
    for dataFind in range(len(data.list)): # goes through list to extract values
        data.centerX = data.list[dataFind][0]
        data.centerY = data.list[dataFind][1]
        data.radius = data.list[dataFind][2]
        drawTarget(canvas,data)
          
# Creates game screen with rectangle with twice the height and width of frame
def gameScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width*2, data.height*2, fill = "white", \
    width = 0)
    canvas.create_rectangle(data.offsetX, data.offsetY, data.width*2 + \
    data.offsetX, data.height*2 + data.offsetY, width = 3)

# Checks event.x and event.y of the mouse click
def mousePressed(event, data):
    if data.gameOver == False: # game play state, does not work when game ends
        list = copy.deepcopy(data.list)
        for dataFind in range (len(list)): # goes through list to extract values
            centerX = list[dataFind][0] + data.offsetTargetX
            centerY = list[dataFind][1] + data.offsetTargetY
            radius = list[dataFind][2]
            distance = math.sqrt((event.x-centerX)**2+(event.y-centerY)**2)
            if distance <= radius: # checks you click within circle
                data.list.remove(data.list[dataFind]) 
                data.score += 1
                # when you click five targets, additional second added
                if data.score % data.numTargetPressed == 0:
                    data.timerCounter -= 1
            
# Defines what happens when pressing a certain key
def keyPressed(event, data):
    if data.gameStart == False: # before starting screen, "p" allows start
        if event.keysym == "p":
            data.gameStart = True
    if data.gameStart == True:
        if event.keysym == "Left": # shifts game screen by 50 to the right
            data.offsetX += data.offset
            data.offsetTargetX += data.offset
        if event.keysym == "Right": # shifts game screen by 50 to the left
            data.offsetX -= data.offset
            data.offsetTargetX -= data.offset
        if event.keysym == "Up": # shifts game screen by 50 downwards
            data.offsetY += data.offset
            data.offsetTargetY += data.offset
        if event.keysym == "Down": # shifts game screen by 50 upwards
            data.offsetY -= data.offset
            data.offsetTargetY -= data.offset
    if data.gameOver == True:  # only allows restart when game over
        if event.keysym == "s":
            # initializes gameStart and gameOver again
            data.gameStart = True
            data.gameOver = False
            data.score = 0
            data.timeLeft = 20
            data.time = 0
            data.timerCounter = 0
            data.list = [[data.centerX, data.centerY, data.radius]]

def timerFired(data):
    if data.gameStart == False: # only in starting screen
        bouncingTarget(data)
    if data.gameStart == True: # when game begins
        data.time += data.timerDelay
        if data.time%data.timeRadius == 0: # targets created every half a second
            radius = random.choice([data.choiceA, data.choiceB, data.choiceC])
            centerX = random.randint(-data.width/2 + data.radius, \
            (data.width*3)/2 - data.radius)
            centerY = random.randint(-data.height/2 + data.radius, \
            (data.height*3)/2 - data.radius)
            data.list += [[centerX, centerY, radius]]
        if data.time%data.timeTimer == 0: # time decreases every second
            data.timerCounter += 1
    # when time ends, game over state
    if data.time >= data.timeEnd and data.timerCounter == 20:
        data.gameOver = True

def bouncingTarget(data):
    if (data.headingRight == True):
        if (data.bounceStartX + data.radius*2 > data.width):
            data.headingRight = False
        else:  data.bounceStartX += 1  # move rightwards
    else:
        if (data.bounceStartX < 0):
            data.headingRight = True
        else:  data.bounceStartX -= 1 # move leftwards
    if (data.headingDown == True):
        if (data.bounceStartY + data.radius*2 > data.height):
            data.headingDown = False
        else:  data.bounceStartY += 1 # move downwards
    else:
        if (data.bounceStartY < 0):
            data.headingDown = True
        else:  data.bounceStartY -= 1 # move upwards

def redrawAll(canvas, data):
    if data.gameStart == False: # starting screen
        startingScreen(canvas, data)
        drawStartingTarget(canvas, data)
        startingText(canvas, data)
    if data.gameStart == True: # begin game
        gameScreen(canvas, data)
        drawGameTarget(canvas, data)
        canvas.create_text(data.margin*2+data.margin, data.margin*2, \
        text="Time Left : " \
        + str(data.timeLeft-data.timerCounter), fill = "darkBlue", \
        font = "Helvetica 18")
        canvas.create_text(data.margin*2+data.margin, data.height- \
        (data.margin*2), \
        text="Score : " + str(data.score), fill = "darkBlue", \
        font = "Helvetica 25")
    if data.gameOver == True: # game over
        canvas.create_rectangle(0, 0, data.width, data.height, fill = "red", \
        width = 0)
        canvas.create_text(data.width/2, data.height/2 - (data.margin*3), \
        text = "GAME OVER!", fill = "white", font = "Helvetica 40 bold")
        canvas.create_text(data.width/2, data.height/2, text = "Final Score: " \
        + str(data.score), fill = "white", font = "Helvetica 25")
        canvas.create_text(data.width/2, data.height/2 + (data.margin*3), \
        text = "Press 's' to start again", fill = "white", font = \
        "Helvetica 25")

####################################
# test functions
####################################

def testBouncingTarget():
    class Struct(object): pass
    data1 = Struct()
    data1.headingRight = True
    data1.headingDown = True
    data1.bounceStartX = 0
    data1.bounceStartY = 0
    data1.radius = 10
    data1.width = 10
    data1.height = 10
    bouncingTarget(data1)
    assert(data1.headingRight == False)
    assert(data1.bounceStartX == 0)
    assert(data1.bounceStartY == 0)
    print ("Test passed!")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


testBouncingTarget()
run(300, 200)

