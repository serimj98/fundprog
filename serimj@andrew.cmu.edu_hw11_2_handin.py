# Homework 11
# Name: Serim Jang
# Andrew ID: serimj

### Gate class and subclasses ###

import cs112_f17_week11_linter
import types

def getLocalMethods(clss):
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class.
    result = [ ]
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

# Main Gate class
class Gate(object):
    def __init__(self): # initializes state to None
        self.oneState = None
        self.twoState = None
        
    def __str__(self):
        typeName = None
        # Assigns typeName for each gate type
        if (type(self).__name__ == "AndGate"):
            typeName = "And"
        elif (type(self).__name__ == "OrGate"):
            typeName = "Or"
        elif (type(self).__name__ == "NotGate"):
            typeName = "Not"
        if self.twoState != None: # if only one state
            return "%s(%s,%s)" % (typeName, self.oneState, self.twoState)
        return "%s(%s)" % (typeName, self.oneState)
        
    def numberOfInputs(self):
        return 2
        
    def setInput(self, x, y):
        if x == 0: # state of first input
            if y == True:
                self.oneState = True
            else:
                self.oneState = False  
        if x == 1: # state of second input
            if y == True:
                self.twoState = True
            else:
                self.twoState = False
    
# When you need both True/True to be True
class AndGate(Gate):
    def getOutput(self):
        if self.oneState == True and self.twoState == True:
            return True
        else:
            return False
   
# When you need at least one state to be True to be True
class OrGate(Gate):
    def getOutput(self):
        if self.oneState == True or self.twoState == True:
            return True
        else:
            return False

# When you need False/False to be True
class NotGate(Gate):
    def getOutput(self):
        if self.oneState == True:
            return False
        else:
            return True
            
    def numberOfInputs(self):
        # overrides number of inputs
        return 1

### ComplexNumber class ###

class ComplexNumber(object):
    def __init__(self, real=0, imaginary=0):
        if isinstance(real, ComplexNumber):
            self.real = real.realPart()
            self.imaginary = real.imaginaryPart()
        else:
            self.real = real
            self.imaginary = imaginary

    def __hash__(self):
        return hash(self.real)
        return hash(self.imaginary)
        
    def __repr__(self):
        # Creates imaginary number equation
        return "%d"%(self.real) + "+%d"%(self.imaginary) + "i"

    def __eq__(self, other):
        if isinstance(other, int): # when instance is an integer
            return self.real == other
        else:
            return isinstance(other, ComplexNumber) and self.real == other.real\
        and self.imaginary == other.imaginary

    def realPart(self):
        return self.real

    def imaginaryPart(self):
        return self.imaginary

    # Sets class attribute to None
    attribute = None

    def getZero():
        if ComplexNumber.attribute == None:
            ComplexNumber.attribute = ComplexNumber()
            return ComplexNumber.attribute
        return ComplexNumber.attribute

### Test Functions ### 

def testGateClasses():
    print("Testing Gate Classes... ", end="")

    # require methods be written in appropriate classes
    assert(getLocalMethods(Gate) == ['__init__', '__str__',
                                     'numberOfInputs', 'setInput'])
    assert(getLocalMethods(AndGate) == ['getOutput'])
    assert(getLocalMethods(OrGate) == ['getOutput'])
    assert(getLocalMethods(NotGate) == ['getOutput', 'numberOfInputs'])

    # make a simple And gate
    and1 = AndGate()
    assert(type(and1) == AndGate)
    assert(isinstance(and1, Gate) == True)
    assert(and1.numberOfInputs() == 2)
    and1.setInput(0, True)
    and1.setInput(1, False)
    # Hint: to get the name of the class given an object obj,
    # you can do this:  type(obj).__name__
    # You might do this in the Gate.__str__ method...
    assert(str(and1) == "And(True,False)")
    assert(and1.getOutput() == False)
    and1.setInput(1, True) # now both inputs are True
    assert(and1.getOutput() == True)
    assert(str(and1) == "And(True,True)")

    # make a simple Or gate
    or1 = OrGate()
    assert(type(or1) == OrGate)
    assert(isinstance(or1, Gate) == True)
    assert(or1.numberOfInputs() == 2)
    or1.setInput(0, False)
    or1.setInput(1, False)
    assert(or1.getOutput() == False)
    assert(str(or1) == "Or(False,False)")
    or1.setInput(1, True)
    assert(or1.getOutput() == True)
    assert(str(or1) == "Or(False,True)")

    # make a simple Not gate
    not1 = NotGate()
    assert(type(not1) == NotGate)
    assert(isinstance(not1, Gate) == True)
    assert(not1.numberOfInputs() == 1)
    not1.setInput(0, False)
    assert(not1.getOutput() == True)
    assert(str(not1) == "Not(False)")
    not1.setInput(0, True)
    assert(not1.getOutput() == False)
    assert(str(not1) == "Not(True)")

    print("Passed!")

def testComplexNumberClass():
    print("Testing ComplexNumber class... ", end="")
    # Do not use the builtin complex numbers in Python!
    # Only use integers!

    c1 = ComplexNumber(1, 2)
    assert(str(c1) == "1+2i")
    assert(c1.realPart() == 1)
    assert(c1.imaginaryPart() == 2)

    c2 = ComplexNumber(3)
    assert(str(c2) == "3+0i") # default imaginary part is 0
    assert(c2.realPart() == 3)
    assert(c2.imaginaryPart() == 0)

    c3 = ComplexNumber()
    assert(str(c3) == "0+0i") # default real part is also 0
    assert(c3.realPart() == 0)
    assert(c3.imaginaryPart() == 0)

    # Here we see that the constructor for a ComplexNumber
    # can take another ComplexNumber, which it duplicates
    c4 = ComplexNumber(c1)
    assert(str(c4) == "1+2i")
    assert(c4.realPart() == 1)
    assert(c4.imaginaryPart() == 2)

    assert((c1 == c4) == True)
    assert((c1 == c2) == False)
    assert((c1 == "Yikes!") == False) # don't crash here
    assert((c2 == 3) == True)

    s = set()
    assert(c1 not in s)
    s.add(c1)
    assert(c1 in s)
    assert(c4 in s)
    assert(c2 not in s)

    assert(ComplexNumber.getZero() == 0)
    assert(isinstance(ComplexNumber.getZero(), ComplexNumber))
    assert(ComplexNumber.getZero() == ComplexNumber())
    # This next one is the tricky part -- there should be one and
    # only one instance of ComplexNumber that is ever returned
    # every time you call ComplexNumber.getZero():
    assert(ComplexNumber.getZero() is ComplexNumber.getZero())
    # Hint: you might want to store the singleton instance
    # of the zero in a class attribute (which you should
    # initialize to None in the class definition, and then
    # update the first time you call getZero()).

    print("Passed!")


##############################################
# testAll and main
##############################################

def testAll():
    testGateClasses()
    testComplexNumberClass()

def main():
    cs112_f17_week11_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
