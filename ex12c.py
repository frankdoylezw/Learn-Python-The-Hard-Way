from sys import argv
AGE = raw_input("How old are you? ")
HEIGHT = raw_input("How tall are you? ")
WEIGHT = raw_input("How much do you weigh? ")
print "So, you're %r old, %r tall and %r heavy." % ( AGE, HEIGHT, WEIGHT)

SCRIPT, FIRST, SECOND = argv

print "You also entered two variables: ", FIRST + " and", SECOND
