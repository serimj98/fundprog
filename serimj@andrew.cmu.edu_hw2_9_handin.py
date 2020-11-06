#################################################
# Hw2
#################################################

import cs112_f17_week2_linter
import math

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

def getKthDigit(n, k):
    return abs(n) // (10**k) % 10

def numberLength(x):
    total = 1
    while x > 9:
        x //= 10
        total += 1
    return total

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

#################################################

def containsOddDigits(x):
    x = abs(x)
    total = 0
    for i in range (numberLength(x)):
        digit = abs(x) // (10**i) % 10
        if digit%2 != 0:
            total += 1
    if total > 0:
        return True
    return False
        
def countMultiplesOfSeven(x, y):
    total = 0
    for i in range (x, y+1):
        if i%7 == 0:
            total += 1
    return total
    
def printNumberTriangle(n):
    total = 0
    for i in range (1, n+1):
        num = total + (i*(10**(i-1)))
        total = num
        print(total)

def sumOfSquaresOfDigits(x):
    total = 0
    for i in range (numberLength(x)):
        num = x%10 #ones digit
        total += num**2
        x = x//10
    return total
    
def isHappyNumber(x):
    print(x)
    if x < 0:
        return False
    s = sumOfSquaresOfDigits(x)
    h = x
    bol = 0
    while x > 1:
        if x == 4:
            return False
        x = sumOfSquaresOfDigits(x)
    if x == 1:
        return True
    return False
    
def nthHappyPrime(n):
    if n == 0:
        return 7
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isHappyNumber(guess) and isPrime(guess):
            found +=1
    return guess

##### Bonus #####

def play112(game):
    return 42

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#################################################
# Test Functions
#################################################

def testContainsOddDigits():
    print('Testing containsOddDigits()... ', end='')
    assert(containsOddDigits(1246) == True)
    assert(containsOddDigits(8663) == True)
    assert(containsOddDigits(224) == False)
    assert(containsOddDigits(115) == True)
    assert(containsOddDigits(8) == False)
    assert(containsOddDigits(9) == True)
    print('Passed!')

def testCountMultiplesOfSeven():
    print('Testing countMultiplesOfSeven()... ', end='')
    assert(countMultiplesOfSeven(3, 16) == 2)
    assert(countMultiplesOfSeven(13, 15) == 1)
    assert(countMultiplesOfSeven(7, 22) == 3)
    assert(countMultiplesOfSeven(8, 28) == 3)
    assert(countMultiplesOfSeven(15, 18) == 0)
    assert(countMultiplesOfSeven(15, 6) == 0)
    print('Passed!')

def testPrintNumberTriangle():
    import sys, io
    print('Testing printNumberTriangle()... ', end='')
    tmpOut = sys.stdout

    oneOutput = io.StringIO()
    sys.stdout = oneOutput
    printNumberTriangle(1)
    oneCheck = oneOutput.getvalue()

    fourOutput = io.StringIO()
    sys.stdout = fourOutput
    printNumberTriangle(4)
    fourCheck = fourOutput.getvalue()

    sevenOutput = io.StringIO()
    sys.stdout = sevenOutput
    printNumberTriangle(7)
    sevenCheck = sevenOutput.getvalue()

    sys.stdout = tmpOut

    assert(oneCheck == "1\n")
    assert(fourCheck == "1\n21\n321\n4321\n")
    assert(sevenCheck == "1\n21\n321\n4321\n54321\n654321\n7654321\n")
    print('Passed!')

def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    print('Passed!')

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# testAll and main
#################################################


def testAll():
    testContainsOddDigits()
    testCountMultiplesOfSeven()
    testPrintNumberTriangle()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyPrime()
    testBonusPlay112()

def main():
    cs112_f17_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
