# 15-112
# Name: Serim Jang
# Andrew ID: serimj

#################################################
# Hw9
#
# No iteration! no 'for' or 'while'.  Also, no 'zip' or 'join'.
# You may add optional parameters
# You may use wrapper functions
#
#################################################

import cs112_f17_week9_linter

def almostEqual(x, y, epsilon = 10**-8):
    return abs(x-y) < epsilon

##############################################
# Recursive questions
##############################################

# Returns the kth power of all numbers below and including n
def powerSum(n, k, current = 1):
    if n <= 0: # when negative number, 0
        return 0
    if k < 0: # when negative number, 0
        return 0
    if current == n: # base case
        return current**k
    if current < n: # recursive case
        return current**k + powerSum(n, k, current+1)

# Helper function to add squares of individual digits in the number
def sumOfSquaresOfDigits(x):
    if x <= 0: # base case; adds nothing if reaches last digit
        return 0
    else: # recursive case; adds square of each digit
        return (x%10)**2 + (sumOfSquaresOfDigits(x//10))

# Returns True if is a happy number
def isHappyNumber(x):
    if x < 0:
        return False
    if x == 1: # definition of happy number
        return True
    if 1 < x < 10 and sumOfSquaresOfDigits(x) != 1: # base case
        return False
    else: # recursive case
        return isHappyNumber(sumOfSquaresOfDigits(x))

# Evalutes prefix notation
def evalPrefixNotation(L):
    if isinstance(L[0], int): # base case
        return L.pop(0)
    if isinstance(L[0], str): # recursive case
        operator = L.pop(0)
        if operator == '+':
            return evalPrefixNotation(L) + evalPrefixNotation(L)
        if operator == '-':
            return evalPrefixNotation(L) - evalPrefixNotation(L)
        if operator == '*':
            return evalPrefixNotation(L) * evalPrefixNotation(L)

##############################################
# OOP questions
##############################################

class VendingMachine(object):

    def __init__(self, bottles, cents):
        self.bottles = bottles
        self.bottleVar = "bottles"
        self.originalCents = cents
        self.cents = cents
        self.paid = 0
        self.left = cents
        self.change = 0
    
    def __hash__(self):
        return hash(self.bottles)
        return hash(self.cents)
    
    def __repr__(self):
        if self.bottles == 1: self.bottleVar = "bottle" # singular
        else: self.bottleVar = "bottles" # plural
        # when no cents, exact dollar amount; when cents, until the cent value
        if self.originalCents % 100 == 0 and self.paid % 100 == 0: 
            return "Vending Machine:<" + "%s "%(self.bottles) + \
            "%s"%(self.bottleVar) + "; $" + "%d"%(self.originalCents/100) +\
             " each; $" + "%d"%(self.paid/100) + " paid>"
        if self.originalCents % 100 == 0 and self.paid % 100 != 0: 
            return "Vending Machine:<" + "%s "%(self.bottles) + \
            "%s"%(self.bottleVar) + "; $" + "%d"%(self.originalCents/100) +\
             " each; $" + "%0.2f"%(self.paid/100) + " paid>"
        if self.originalCents % 100 != 0 and self.paid % 100 == 0: 
            return "Vending Machine:<" + "%s "%(self.bottles) + \
            "%s"%(self.bottleVar) + "; $" + "%0.2f"%(self.originalCents/100) +\
             " each; $" + "%d"%(self.paid/100) + " paid>"
        if self.originalCents % 100 != 0 and self.paid % 100 != 0:
            return "Vending Machine:<" + "%s "%(self.bottles) + \
            "%s"%(self.bottleVar) + "; $" + "%0.2f"%(self.originalCents/100) +\
             " each; $" + "%0.2f"%(self.paid/100) + " paid>"
            
    def __eq__(self,other):
        # all numbers within the class VendingMachine should be equal
        return isinstance(other, VendingMachine) and \
        self.bottles == other.bottles and self.bottleVar == other.bottleVar \
        and self.originalCents == other.originalCents and \
        self.cents == other.cents and self.paid ==other.paid and \
        self.left == other.left and self.change == other.change

    def isEmpty(self):
        if self.bottles != 0: # when no bottles, isEmpty
            self.paid = 0
            return False
        else:
            return True

    def getBottleCount(self):
        return self.bottles # number of bottles
    
    def stillOwe(self):
        if self.bottles == 0: # returns amount you paid if no bottles
            self.left = self.originalCents
            return self.originalCents
        else: # if bottles exist, the money you still need to put in
            return self.left
    
    def insertMoney(self, insert):
        self.left -= insert
        self.paid += insert
        if self.left == 0: # when you put in the full amount
            self.cents = 0
            self.bottles -= 1
            self.left = self.originalCents
            self.paid = 0
            return ("Got a bottle!", self.change)
        if self.bottles == 0: # when no bottles
            return ("Machine is empty", insert)
        if self.left < 0: # when you put in extra money
            self.change = abs(self.left)
            self.cents = self.change
            self.bottles -= 1
            self.left = self.originalCents
            return ("Got a bottle!", self.change)
        if self.left % 100 == 0: # when no cents, return exact dollar amount
            return ("Still owe $" + "%d"%(int(self.left/100)), self.change)
        else: # when cents, returns until the cent value
            return ("Still owe $" + "%.2f"%(self.left/100), self.change)

    def stockMachine(self, stock):
        self.bottles += stock # adds bottles to the stock
        
#################################################
# Test Functions
#################################################

def testPowerSum():
    print('Testing powerSum()...', end='')
    assert(powerSum(4, 6) == 1**6 + 2**6 + 3**6 + 4**6)
    assert(powerSum(0, 6) == 0)
    assert(powerSum(4, 0) == 1**0 + 2**0 + 3**0 + 4**0)
    assert(powerSum(4, -1) == 0)
    print('Done!')

def testIsHappyNumber():
    print('Testing isHappyNumber()...', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Done!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    print('Done!')

def testVendingMachineClass():
    print("Testing Vending Machine class...", end="")
    # Vending machines have three main properties: 
    # how many bottles they contain, the price of a bottle, and
    # how much money has been paid. A new vending machine starts with no
    # money paid.
    vm1 = VendingMachine(100, 125)
    assert(str(vm1) == "Vending Machine:<100 bottles; $1.25 each; $0 paid>")
    assert(vm1.isEmpty() == False)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.stillOwe() == 125)

    # When the user inserts money, the machine returns a message about their
    # status and any change they need as a tuple.
    assert(vm1.insertMoney(20) == ("Still owe $1.05", 0))
    assert(vm1.stillOwe() == 105)
    assert(vm1.getBottleCount() == 100)
    assert(vm1.insertMoney(5) == ("Still owe $1", 0))
    
    # When the user has paid enough money, they get a bottle and 
    # the money owed resets.
    assert(vm1.insertMoney(100) == ("Got a bottle!", 0))
    assert(vm1.getBottleCount() == 99)
    assert(vm1.stillOwe() == 125)
    assert(str(vm1) == "Vending Machine:<99 bottles; $1.25 each; $0 paid>")
    
    # If the user pays too much money, they get their change back with the
    # bottle.
    assert(vm1.insertMoney(500) == ("Got a bottle!", 375))
    assert(vm1.getBottleCount() == 98)
    assert(vm1.stillOwe() == 125)
    
    # Machines can become empty
    vm2 = VendingMachine(1, 120)
    assert(str(vm2) == "Vending Machine:<1 bottle; $1.20 each; $0 paid>")
    assert(vm2.isEmpty() == False)
    assert(vm2.insertMoney(120) == ("Got a bottle!", 0))
    assert(vm2.getBottleCount() == 0)
    assert(vm2.isEmpty() == True)
    
    # Once a machine is empty, it should not accept money until it is restocked.
    assert(str(vm2) == "Vending Machine:<0 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Machine is empty", 25))
    assert(vm2.insertMoney(120) == ("Machine is empty", 120))
    assert(vm2.stillOwe() == 120)
    vm2.stockMachine(20) # Does not return anything
    assert(vm2.getBottleCount() == 20)
    assert(vm2.isEmpty() == False)
    assert(str(vm2) == "Vending Machine:<20 bottles; $1.20 each; $0 paid>")
    assert(vm2.insertMoney(25) == ("Still owe $0.95", 0))
    assert(vm2.stillOwe() == 95)
    vm2.stockMachine(20)
    assert(vm2.getBottleCount() == 40)

    # We should be able to test machines for basic functionality
    vm3 = VendingMachine(50, 100)
    vm4 = VendingMachine(50, 100)
    vm5 = VendingMachine(20, 100)
    vm6 = VendingMachine(50, 200)
    vm7 = "Vending Machine"
    assert(vm3 == vm4)
    assert(vm3 != vm5)
    assert(vm3 != vm6)
    assert(vm3 != vm7) # should not crash!
    s = set()
    assert(vm3 not in s)
    s.add(vm4)
    assert(vm3 in s)
    s.remove(vm4)
    assert(vm3 not in s)
    assert(vm4.insertMoney(50) == ("Still owe $0.50", 0))
    assert(vm3 != vm4)
    
    print("Done!")

##############################################
# testAll and main
##############################################

def testAll():
    testPowerSum()
    testIsHappyNumber()
    testEvalPrefixNotation()
    testVendingMachineClass()

def main():
    #cs112_f17_week9_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
