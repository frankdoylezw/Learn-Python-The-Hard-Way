"""Exercise 24
"""
import os
os.system('clear')

print "Let's practise everything."
print '\nYou\'d need to know \'bout escapes with \\ that to do \n newlines and \t tabs.'

POEM = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "\n********************"
print POEM
print "********************\n"

FIVE = 10 - 2 + 3 - 6
print "This should be five: %s" % FIVE

def secret_formula(started):
    """This is a function docstring"""
    JELLYBEANS = started * 500
    JARS = JELLYBEANS / 1000
    CRATES = JARS / 100
    return JELLYBEANS, JARS, CRATES

START_POINT = 10000
beans, jars, crates = secret_formula(START_POINT)

print "With a starting point of %d" % START_POINT
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

START_POINT = START_POINT / 10

print "We can also do it this way:"
print " We'd have %d beans, %d jars and %d crates." % secret_formula(START_POINT)
print "\n"
