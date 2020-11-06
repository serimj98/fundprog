#################################################
# Hw1
#################################################

import cs112_f17_linter
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

#################################################
# Hw1 problems
#################################################

def hotdogPurchase(numHotdogs):
    return math.ceil(numHotdogs / 10), math.ceil(numHotdogs / 8)

def hotdogExcess(numHotdogs): 
    return (math.ceil(numHotdogs / 10)*10 - numHotdogs), \
    (math.ceil(numHotdogs / 8)*8 - numHotdogs)

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    len1 = distance (x1, y1, x2, y2)
    len2 = distance (x1, y1, x3, y3)
    len3 = distance (x2, y2, x3, y3)
    if almostEqual(len1**2 + len2**2, len3**2):
        return True
    if almostEqual(len2**2 + len3**2, len1**2):
        return True
    if almostEqual(len3**2 + len1**2, len2**2):
        return True
    else:
        return False

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def lineIntersection(m1, b1, m2, b2):
    if (m1 - m2 == 0):
        return None
    if (b2 - b1 == 0):
        return 0
    if (b2 - b1 != 0):
        return ((b2 - b1) / (m1 - m2))

def triangleArea(s1, s2, s3):
    if s1 <=0 or s2 <=0 or s3 <=0:
        return False
    S = (s1 + s2+ s3) / 2
    return math.sqrt (S*(S - s1) * (S - s2) * (S - s3))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1, b1, m2, b2)
    x2 = lineIntersection(m2, b2, m3, b3)
    x3 = lineIntersection(m1, b1, m3, b3)
    y1 = m1*x1 + b1
    y2 = m2*x2 + b2
    y3 = m3*x3 + b3
    s1 = abs(distance(x1, y1, x2, y2))
    s2 = abs(distance(x1, y1, x3, y3))
    s3 = abs(distance(x2, y2, x3, y3))
    return triangleArea(s1, s2, s3)

def bonusFindIntRootsOfCubic(a, b, c, d):
    return 42

#################################################
# Hw1 Test Functions
#################################################

def testHotdogPurchase():
    print('Testing hotdogPurchase()... ', end='')
    assert(hotdogPurchase(0) == (0,0))
    assert(hotdogPurchase(13) == (2,2))
    assert(hotdogPurchase(26) == (3,4))
    assert(hotdogPurchase(39) == (4,5))
    assert(hotdogPurchase(50) == (5,7))
    assert(hotdogPurchase(61) == (7,8))
    assert(hotdogPurchase(80) == (8,10))
    assert(hotdogPurchase(88) == (9,11))
    print('Passed.')

def testHotdogExcess():
    print('Testing hotdogExcess()... ', end='')
    assert(hotdogExcess(0) == (0,0))
    assert(hotdogExcess(13) == (7,3))
    assert(hotdogExcess(26) == (4,6))
    assert(hotdogExcess(39) == (1,1))
    assert(hotdogExcess(50) == (0,6))
    assert(hotdogExcess(61) == (9,3))
    assert(hotdogExcess(80) == (0,0))
    assert(hotdogExcess(88) == (2,0))
    print('Passed.')
 
def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def testAll():
    testHotdogPurchase()
    testHotdogExcess()
    testIsRightTriangle()
    testDistance()
    testLineIntersection()
    testTriangleArea()
    testThreeLinesArea()
    testBonusFindIntRootsOfCubic()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_f17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
