import cs112_f17_week5_linter
from tkinter import *
from sudoku import *
import copy, math

#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################

def init(data):
    data.boardLen = 9
    data.original = copy.deepcopy(data.board)
    data.highlightCol = 0
    data.highlightRow = 0
    data.colRowList = []
    data.begin = 0
    data.over = 0

def keyPressed(event, data):
    # Disable keys when board is filled
    data.over = 0
    for row in range (data.boardLen):
        for col in range (data.boardLen):
            if data.board[row][col] == 0:
                data.over = 1
    if data.over == 0:
        return None
    # When pressing left, right, down, and up, should change highlighted box
    if event.keysym == "Right":
        data.highlightCol += 1
    elif event.keysym == "Left":
        data.highlightCol -= 1
    elif event.keysym == "Down":
        data.highlightRow += 1
    elif event.keysym == "Up":
        data.highlightRow -= 1
    # Checks that the symbol pressed is a digit
    elif (event.keysym).isdigit():
        if data.original[data.highlightRow][data.highlightCol] == 0:
            data.board[data.highlightRow][data.highlightCol] = int(event.keysym)
            data.colRowList+=[(data.highlightRow, data.highlightCol)]
    # Checks whether the values entered results in a legal Sudoku
    if not(isLegalSudoku(data.board)):
        data.board[data.highlightRow][data.highlightCol] = 0
    # Allows BackSpace to delete value entered
    if event.keysym == "BackSpace":
        data.board[data.highlightRow][data.highlightCol] = 0

def drawBoard(canvas, data):
    margin = 20
    width = data.width - 2*margin
    height = data.height - 2*margin
    # Highlights the boxes
    for row in range (int(data.boardLen/3)):
        for col in range (int(data.boardLen/3)):
            x2 = margin + (width/int(data.boardLen/3))*col
            y2 = margin + (height/int(data.boardLen/3))*row
            x3 = margin + (width/int(data.boardLen/3))*(col+1)
            y3 = margin + (height/int(data.boardLen/3))*(row+1)  
            canvas.create_rectangle(x2, y2, x3, y3, fill="white", width=3)
    # Creates 9X9 board
    for row in range (data.boardLen):
        for col in range (data.boardLen):
            x0 = margin + (width/data.boardLen)*col
            y0 = margin + (height/data.boardLen)*row
            x1 = margin + (width/data.boardLen)*(col+1)
            y1 = margin + (height/data.boardLen)*(row+1)
            canvas.create_rectangle(x0, y0, x1, y1, width=1)

def highlightBox(canvas, data):
    margin = 20
    width = data.width - 2*margin
    height = data.height - 2*margin
    # Keeps highlight box inside board
    if data.highlightCol > data.boardLen-1:
        data.highlightCol = 0
    if data.highlightCol < 0:
        data.highlightCol = data.boardLen-1
    if data.highlightRow > data.boardLen-1:
        data.highlightRow = 0
    if data.highlightRow < 0:
        data.highlightRow = data.boardLen-1
    # Creates highlight box
    x0 = margin + (width/data.boardLen)*data.highlightCol
    y0 = margin + (height/data.boardLen)*data.highlightRow
    x1 = margin + (width/data.boardLen)*(data.highlightCol+1)
    y1 = margin + (height/data.boardLen)*(data.highlightRow+1)
    canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", width=1)

def newNumbers(canvas, data):
    margin = 20
    width = data.width - 2*margin
    height = data.height - 2*margin
    # Adds new numbers to the board in black
    for lst in data.colRowList:
        col = lst[1]
        row = lst[0]
        x0 = margin + (width/data.boardLen)*col
        y0 = margin + (height/data.boardLen)*row
        x1 = margin + (width/data.boardLen)*(col+1)
        y1 = margin + (height/data.boardLen)*(row+1)
        # Disables 0 values on the board
        if data.board[row][col] == 0:
            text=""
        else:
            text = data.board[row][col]
            canvas.create_text((x0+x1)/2, (y0+y1)/2, text=text, font="Helvetica 18", fill="black")
        
def showNumbers(canvas, data):
    margin = 20
    width = data.width - 2*margin
    height = data.height - 2*margin
    # Reflects values in 2D list onto the board in blue
    for row in range (data.boardLen):
        for col in range (data.boardLen):
            x0 = margin + (width/data.boardLen)*col
            y0 = margin + (height/data.boardLen)*row
            x1 = margin + (width/data.boardLen)*(col+1)
            y1 = margin + (height/data.boardLen)*(row+1)
            if data.original[row][col] == 0:
                text=""
            else:
                text = data.original[row][col]
                canvas.create_text((x0+x1)/2, (y0+y1)/2, text=text, font="Helvetica 18", fill="blue")
    data.begin = 1

def endGame(canvas, data):
    margin = 20
    width = data.width - 2*margin
    height = data.height - 2*margin
    data.over = 0
    for row in range (data.boardLen):
        for col in range (data.boardLen):
            # Checks whether 0 values are in the 2D list
            if data.board[row][col] == 0:
                data.over = 1
    # If there are no 0s on the board, print "You Win!"
    if data.over == 0:
        canvas.create_text(width/2, height/2, text="You Win!", font="Helvetica 70", fill="green")

def redrawAll(canvas, data):
    margin = 20
    drawBoard(canvas,data)
    highlightBox(canvas,data)
    showNumbers(canvas,data)
    newNumbers(canvas, data)
    endGame(canvas, data)
    
########################################
# Do not modify the playSudoku function.
########################################

def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard

    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    
    board = [
            [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
        ]
    
    # board = [
    #         [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
    #         [ 5, 0, 8, 1, 3, 9, 6, 2, 4 ],
    #         [ 4, 9, 6, 8, 7, 2, 1, 5, 3 ],
    #         [ 9, 5, 2, 3, 8, 1, 4, 6, 7 ],
    #         [ 6, 4, 1, 2, 9, 7, 8, 3, 5 ],
    #         [ 3, 8, 7, 5, 6, 4, 0, 9, 1 ],
    #         [ 7, 1, 9, 6, 2, 3, 5, 4, 8 ],
    #         [ 8, 6, 4, 9, 1, 5, 3, 7, 2 ],
    #         [ 2, 3, 5, 7, 4, 8, 9, 1, 6 ]
    #     ]
    playSudoku(board)

if __name__ == '__main__':
    main()
