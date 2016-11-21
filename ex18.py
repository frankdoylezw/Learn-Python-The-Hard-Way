
"""Exercise 18
http://learnpythonthehardway.org/book/ex18.html
"""
import os
os.system('clear')

#this one is like your scripts with argv

"""This function takes two arguments an prints them
"""
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#This just takes a single argument
def print_one(arg1):
    print "arg1: %r" % arg1

#This one takes no arguments
def print_none():
    print "I got nothin'."

print_two('Frank', 'Doyle')
print_two_again("Frank", "Doyle")
print_one("First!")
print_none()
