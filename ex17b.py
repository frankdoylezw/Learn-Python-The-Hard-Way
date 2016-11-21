"""This is the DOCSTRING"""

import os
from os.path import exists
os.system('clear')

STARTFILE = raw_input("Enter the name of the file you want to copy from: ")
ENDFILE = raw_input("Enter the destination file: ")

print "Now copying from %s to %s." % (STARTFILE, ENDFILE)

INFILE = open(STARTFILE)
INDATA = INFILE.read()

print "I've opened the file and read the data in it."
print "It is %d bytes long" % len(INDATA)
print "Does the destination file exist? %r" % exists(ENDFILE)

print "READY TO COPY? Hit RETURN to continue, CTRL-C to abort"
raw_input()

OUTFILE = open(ENDFILE, 'w')
OUTFILE.write(INDATA)


print "OK. That's all done for you."


OUTFILE.close()
INFILE.close()

print "\nTime to print out the contents of the file: "
TARGET = open(ENDFILE, 'r')
print "\n"
print TARGET.read()

TARGET.close()
