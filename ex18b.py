"""
This is the second of the EX18 files
"""
import os
os.system('clear')

ARG1A = raw_input("What is your ARG1 called? ")
ARG2A = raw_input("What is your ARG2 called? ")
ARG3A = raw_input("What is your ARG3 called? ")

def firstfunction(ARG1, ARG2):
    """This is the first function"""
    print "ARG1A = %r, ARG2A = %r" % (ARG1A, ARG2A)

def secondfunction(ARG3):
    """This is the second function"""
    print "ARG3A = %r" % (ARG3A)

firstfunction(ARG1A, ARG2A)
secondfunction(ARG3A)
