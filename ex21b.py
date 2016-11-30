"""
Exercise 21 Revisited
"""
import os
os.system('clear')

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some maths just with functions!"

AGE = add(25, 13)
HEIGHT = subtract(198, 10)
WEIGHT = multiply(40, 2)
IQ = divide(100, 2)

print "AGE: %d, HEIGHT: %d, WEIGHT: %d, IQ: %d" % (AGE, HEIGHT, WEIGHT, IQ)

#A puzzle for extra credit, type it in anyway.

print "Here is a puzzle: "

WHAT = add(AGE, subtract(HEIGHT, multiply(WEIGHT, divide(IQ, 2))))

print "That becomes: ", WHAT, "Can you do it by hand? Nope, thought not!"
