# 15-112
# Name: Serim Jang
# Andrew ID: serimj

import cs112_f17_week10_linter

### Homework 10 ###

# Returns single list from containing lists
def flatten(L, flattened = None):
    if flattened == None:
        flattened = []
    if not isinstance(L, list): # if not a list, return value
        flattened.append(L)
        if str(L).isdigit():
            return L
        return None
    if len(L) == 0: # when the list is empty
        return []
    else:
        for elem in L: # checks each element in L
            flatten(elem, flattened)
        return flattened
    return flattened    

# Returns none if there is an error (uses function decorator)
def noError(f):
    def g(*args):
        try: # if no error
            return f(*args)
        except: # error
            return None
    return g

# Solves the ABC puzzle
def solveABC(constraints, aLocation):
    visited = set()
    (row,col) = aLocation
    
    # Creates the solution board without allowing aliases
    def makeBoard():
        rowList = []
        board = []
        boardLength = 5
        for row in range(boardLength):
            for col in range(boardLength):
                rowList.append(-1)
            board.append(rowList)
            rowList=[]
        return board
        
    # Creates the alphabet board without allowing aliases
    def makeLstBoard():
        innerLst=[]
        outerLst=[]
        boardLength = 5
        for row in range(boardLength):
            for col in range(boardLength):
                innerLst.append([])
            outerLst.append(innerLst)
            innerLst=[]
        return outerLst
        
    # Creates list with all constraints for each cell
    def makeAlphabetBoard(constraints):
        iteration = 5
        top = 6
        right = 12
        alphabetBoard = makeLstBoard()
        for fill in range(len(constraints)//2):
            if fill > 0 and fill < top: 
                alphabetBoard=alphabetTopBottom(alphabetBoard,
                    iteration, fill, constraints)
            if fill > top and fill < right:
                alphabetBoard=alphabetLeftRight(alphabetBoard,
                    iteration, fill, constraints)
            else:
                alphabetBoard=alphabetDiagonal(alphabetBoard,
                    iteration, fill, constraints)
        return alphabetBoard
    
    # Checks alphabet constraints from top to bottom
    def alphabetTopBottom(alphabetBoard, iteration, fill, constraints):
        topBottom = 18
        for row in range(iteration): # adds constraints top/bottom
            alphabetBoard[row][fill-1].append(constraints[fill])
            alphabetBoard[row][fill-1].append(constraints[topBottom-fill])
        return alphabetBoard
      
    # Checks alphabet constraints from left to right    
    def alphabetLeftRight(alphabetBoard, iteration, fill, constraints):
        leftRight = 30
        row = 5
        for col in range(iteration): # adds constraints left/right
            alphabetBoard[fill-1-leftRight//row][col].append(constraints[fill])
            alphabetBoard[fill-1-leftRight//row][col].append(constraints
                                                            [leftRight-fill])
        return alphabetBoard
    
    # Checks alphabet constraints from that are diagonal
    def alphabetDiagonal(alphabetBoard, iteration, fill, constraints):
        leftDiagonal = 12
        rightDiagonal = 24
        top = 6
        rangeRow = 4
        if fill == 0: # diagonal top/left, bottom/right
            for diagonal in range(iteration):
                alphabetBoard[diagonal][diagonal].append(constraints[fill])
                alphabetBoard[diagonal][diagonal].append(constraints\
                    [leftDiagonal-fill])
        if fill == top: #diagonal top/right, bottom/left
            for diagonal in range(iteration):
                alphabetBoard[diagonal][rangeRow-diagonal].append\
                    (constraints[fill])
                alphabetBoard[diagonal][rangeRow-diagonal].append(constraints\
                    [rightDiagonal-fill])     
        return alphabetBoard
        
    solution = makeBoard()
    solution[row][col]="A"
    constraint=makeAlphabetBoard(constraints)
    
    # Check if the puzzle is full
    def isFullABC(board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == -1:
                    return False
        return True

    # Checks legality of next move
    def isLegalABC(constraint, testRow, testCol, solution, alphabet, visited):
        # check if on board
        if not(0 <= testRow < len(solution) 
                        and 0 <= testCol < len(solution[0])):
            return False
        # check if in constraints
        elif alphabet not in constraint[testRow][testCol]:
            return False
        # if already visited
        elif (testRow, testCol) in visited:
            return False
        # if value already exists
        elif solution[testRow][testCol]!=-1:
            return False
        return True
    
    # Solves puzzle using backtracking
    def solve(testRow, testCol, solution, constraint, alphabet="B"):
        direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        if isFullABC(solution): # if full board, return solution
            return solution
        else:
            for move in direction: # checks all possible moves
                testRow,testCol=testRow+move[0],testCol+move[1]
                # checks if legal
                if isLegalABC(constraint,testRow,testCol,solution, 
                                                            alphabet, visited):
                    visited.add((testRow,testCol))
                    solution[testRow][testCol]=alphabet
                    board=solve(testRow,testCol,solution, constraint, \
                        chr(ord(alphabet)+1))
                    # found next move is available
                    if board != None:
                        return board
                    # undo move
                    visited.remove((testRow,testCol))
                    solution[testRow][testCol]=-1
                # resets testRow, testCol
                testRow, testCol=testRow-move[0],testCol-move[1]
    return solve(row,col,solution, constraint)

### hFractal() ###

from tkinter import *

def init(data):
    data.level = 0

def keyPressed(event, data):
    if event.keysym == "Up":
        data.level += 1
    if event.keysym == "Down":
        if data.level > 0:
            data.level -= 1

def timerFired(data):
    pass

def mousePressed(event, data):
    pass

def drawH(canvas, x, y, sideOne, sideTwo):
    midY=y+(sideTwo//2)
    canvas.create_line(x, midY, x+sideOne, midY, width = 3) # central line
    canvas.create_line(x, y, x,y+sideTwo,width=3) # left line
    canvas.create_line(x+sideOne,y,x+sideOne,y+sideTwo, width=3) # right line

def redrawAll(canvas, data):
    side=7/20
    x=(data.width-sideOne)//2
    y=(data.height-sideTwo)//2
    fractalH(canvas, x, y, data.width*side, data.height*side, data.level)

def fractalH(canvas, x, y, sideOne, sideTwo, level=0):
    smallFractal = 4
    halfFractal = 2
    if level == 0: # when level 0, just H
        drawH(canvas, x, y, sideOne, sideTwo)
    else: # adds H with extra level
        fractalH(canvas,x,y,sideOne,sideTwo,level-1)
        fractalH(canvas, x-(sideOne//smallFractal), y-(sideTwo//smallFractal), \
                    sideOne//halfFractal, sideTwo//halfFractal, level-1)
        fractalH(canvas, x+sideOne-(sideOne//smallFractal), \
            y-(sideTwo//smallFractal), sideOne//halfFractal, \
            sideTwo//halfFractal, level-1)
        fractalH(canvas, x-(sideOne//smallFractal), \
            y+(sideTwo-sideTwo//smallFractal), sideOne//halfFractal, \
            sideTwo//halfFractal, level-1)
        fractalH(canvas, x+sideOne-(sideOne//smallFractal), \
            y+(sideTwo-sideTwo//smallFractal), sideOne//halfFractal, \
            sideTwo//halfFractal, level-1)

def hFractal():
    run(600, 400)

####################################
# use the run function as-is
####################################

def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, width, height,
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
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

### Test Functions ###

def testFlatten():
    print("Testing flatten()...", end="")
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten(3) == 3)
    print("Passed!")

def testNoErrorDecorator():
    print("Testing @noError decorator...", end="")
    @noError
    def f(x, y): return x/y
    assert(f(1, 5) == 1/5)
    assert(f(1, 0) == None)

    @noError
    def g(): return 1/0
    assert(g() == None)

    @noError
    def h(n):
        if (n == 0): return 1
        else: return h(n+1)
    assert(h(0) == 1)
    assert(h(-1) == 1)
    assert(h(1) == None)

    print("Passed!")

def testSolveABC():
    print('Testing solveABC()...', end='')
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)
    print('Passed!')

##############################################
# testAll and main
##############################################

def testAll():
    pass

def main():
    # cs112_f17_week10_linter.lint() # check style rules
    hFractal()
    testAll()

if __name__ == '__main__':
    main()
