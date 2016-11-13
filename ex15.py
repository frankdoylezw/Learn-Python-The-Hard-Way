
#Here we're importing the argv module
#from sys import argv

#Specifying the variables that comprise argv
#SCRIPT, FILENAME = argv

FILENAME = raw_input("Enter the name of the file you are trying to enter: ")

"""Here we're using the open command, passing in the parameter of 
FILENAME, and calling it TXT
"""
TXT = open(FILENAME)

print "Here's your file %r: " % FILENAME
#Now, because we created TXT, we can use the file methods like .read()
print TXT.read()

#Asks the user to re-input the filename
print "Type the filename again:"
FILE_AGAIN = raw_input("> ")


#Once you have the filename, use the open command again
TXT_AGAIN = open(FILE_AGAIN)

print TXT_AGAIN.read()

TXT_AGAIN.close
TXT.close

