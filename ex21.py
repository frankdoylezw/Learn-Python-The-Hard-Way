"""Exercise 21: Setting variables to be a value from a #unction"""

import os
os.system('clear')

def add(a, b):
    """This function adds two numbers and assigns the result to a variable"""
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

########################################################
print "Let's do some mathematics with just FUNCTIONS!!!"

AGE = add(30, 5)
HEIGHT = subtract(78, 4)
WEIGHT = multiply(90, 2)
IQ = divide(100, 2)

print "Age: %d, Height: %d, Weight %d, IQ: %d" % (AGE, HEIGHT, WEIGHT, IQ)

print "Here is a puzzle: "

WHAT = add(AGE, subtract(HEIGHT, multiply(WEIGHT, divide(IQ, 2))))

print "That becomes: ", WHAT, "Can you do it by hand?"
