"""Exercise 20: Functions and FIles"""
import os
#from sys import argv
os.system('clear')

#script, INPUT_FILE = argv
INPUT_FILE = raw_input("What is the name of your text file? ")
def print_all(F):
    """This function reads the entire file."""
    print F.read()

def rewind(F):
    #This function seeks the cursor position to 0"""
    F.seek(0)

def print_a_line(line_count, F):
    """This function takes two parameters - a line and the file.
    It then prints out the line number, and reads the line from the file"""
    print line_count, F.readline()

#This opens a file ready for reading. NB - we set the INPUT_FILE variable up above.
CURRENT_FILE = open(INPUT_FILE)

print "First let's print the whole file: \n"
print_all(CURRENT_FILE)

print "Now let's rewind, kind of like a tape: \n"
rewind(CURRENT_FILE)

print "Let's print three lines: \n"

CURRENT_LINE = 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE += 1
print_a_line(CURRENT_LINE, CURRENT_FILE)

CURRENT_LINE += 1
print_a_line(CURRENT_LINE, CURRENT_FILE)
