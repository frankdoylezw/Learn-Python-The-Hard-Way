"""This is the DOCSTRING"""
from sys import argv
import os
from os.path import exists

os.system('clear')

FROM = raw_input("Enter the file to copy FROM: ")
TO = raw_input("Enter the name of the file to copy TO: ")

print "Copying from %s to %s" % (FROM, TO)

IN_FILE = open(FROM)
INDATA = IN_FILE.read()

print "The FROM file is %d bytes long" % len(INDATA)
print "Ready? Hit RETURN to continue, CTRL-C to abort."
raw_input()

OUT_FILE = open(TO, 'w')
OUT_FILE.write(INDATA)
print "Alright, that's done."

OUT_FILE = open(TO, 'w')
OUTDATA = OUT_FILE.read()
print "The TO file is %d bytes long, now." % len(OUTDATA)


OUT_FILE.close()
IN_FILE.close()
