"""Exercise 20: Functions and Files"""
import os
os.system('clear')

def print_two(*args):
    """Function docstrings explain what your function is to
    be used for"""
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#OK, that's a long-winded way of writing a function. Do this instead:
def print_two_again(arg1, arg2):
    """Simple function to print function arguments"""
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#This one just takes a single argument
def print_one(arg1):
    """Funcion docstring"""
    print "arg1: %r" % (arg1)

#This one takes no arguments
def print_none():
    """Function docstrng"""
    print "I got nuthin'."

print_two("Frank", "Doyle")
print_two_again("Frank", "Doyle")
print_one("This is the one and only argument I'm printing!")
print_none()
