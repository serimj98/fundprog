#################################################
# Hw4
#################################################

import cs112_f17_week4_linter
import math, string, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Problems
#################################################

# This is supposed to remove blank lines and comments.
# It has some bugs though...

def buggyCleanUpCode(code):
    lines = code.splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i]
        # Get rid of blank lines
        if ((lines[i] in string.whitespace) or (lines[i].startswith("#"))):
            lines[i] = ""
        else:
            # Get rid of comments
            commentIndex = lines[i].find("#")
            if commentIndex<0:
                lines[i] = lines[i] + "\n"
            else:
                if i == len(lines)-1:
                    lines[i] = lines[i][:commentIndex] 
                else:
                    lines[i] = lines[i][:commentIndex] +"\n"
        return "".join(lines)

def computeScore(word, letterScores):
    # calculates score
    score = 0
    for letter in word:
        score += letterScores[ord(letter)-ord("a")]
    return score
    
def validWord(word, hand):
    # finds if word is possible
    for letter in word:
        if not(letter in hand):
            return False
        hand[hand.index(letter)] = ""
    return True
    
def bestScrabbleScore(dictionary, letterScores, hand):
    currWord = ""
    currScore = 0
    heighestWord = []
    heightestScore = 0
    for word in dictionary:
        a = copy.copy(hand)
        if validWord(word, a): 
            currScore = computeScore(word, letterScores)
            currWord = word
            if currScore > heightestScore: # finds highest score
                heightestScore = currScore
                heighestWord = [currWord]
            elif currScore == heightestScore:
                heighestWord.extend([currWord])
    if len(heighestWord) == 1:
        return(heighestWord[0], heightestScore)
    elif len(heighestWord) == 0:
        return None
    else:
        return (heighestWord, heightestScore)

###### Autograded Bonus ########
# (place non-autograded bonus below #ignore-rest line!) #

def runSimpleProgram(program, args):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

from tkinter import *
import math

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    root = Tk()
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    canvas.create_text(10, 0, text=program, anchor=NW, fill='gray', font="Helvetica 10")
    color, move, left, right, theta = [], [], [], [], 0
    moveVal, colorVal, leftVal, rightVal = "", "", "", ""
    endX, endY = 0, 0
    program = buggyCleanUpCode(program)
    program = program.splitlines()
    startX = winWidth/2
    startY = winHeight/2
    for i in range(len(program)):
        if "color" in program[i]: # sets color of line
            colorVal = program[i].replace("color ","")
            colorVal = colorVal.strip()
            if colorVal == "none":
                color = "white"
            else:
                color = colorVal
        # finds left/right
        elif "left" in program[i]:
            leftVal = program[i].replace("left ","")
            theta += float(leftVal)
        elif "right" in program[i]:
            rightVal = program[i].replace("right ","")
            theta -= float(rightVal)
        elif "move" in program[i]: # finds the number to move
            moveVal = program[i].replace("move ","")
            move = float(moveVal)
            endX = startX + move*math.cos(math.radians(theta))
            endY = startY - move*math.sin(math.radians(theta))
            canvas.create_line(startX, startY, endX, endY, fill = color, width = 4)
            startX = endX
            startY = endY
    root.mainloop()

def testRunSimpleTortoiseProgram1():
    runSimpleTortoiseProgram("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""", 300, 400)

def testRunSimpleTortoiseProgram2():
    runSimpleTortoiseProgram("""
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
""")

def testRunSimpleTortoiseProgram():
    print("Testing runSimpleTortoiseProgram()...")
    print("Since this is graphics, this test is not interactive.")
    print("Inspect each of these results manually to verify them.")
    testRunSimpleTortoiseProgram1()
    testRunSimpleTortoiseProgram2()
    print("Done!")

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    testBestScrabbleScore()
    testRunSimpleTortoiseProgram()
    testRunSimpleProgram()

def main():
    cs112_f17_week4_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
