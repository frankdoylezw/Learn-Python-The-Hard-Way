"""
This is the DOCSTRING
"""

from sys import argv
import os

os.system('clear')

#Defining the SCRIPT and FILENAME variables
SCRIPT = argv
FILENAME = raw_input("Enter the name of your file: ")

print "We're going to erase %r." % FILENAME
print "If you don't want to do that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."
#Use raw_input when you need input of some sort.
raw_input("?")

print "Opening the file..."
TARGET = open(FILENAME, 'w')

print "Truncating the file...Goodbye!"
TARGET.truncate()

print "Now I'm going to ask you for three lines, BIATCH!"

LINE1 = raw_input("LINE1:   ")
LINE2 = raw_input("LINE2:   ")
LINE3 = raw_input("LINE3:   ")

print "I'm going to write those lines to a file"

TARGET.write(LINE1 + "\n" + LINE2 + "\n" + LINE3 + "\n")

print "And finally...we close it."
TARGET.close()

#Read and print the contents of the file
print "\nTime to print out the contents of the file:"
TARGET = open(FILENAME, 'r')
print TARGET.read()
TARGET.close()
