'''This is a docstring'''

NAME = raw_input('Hello, what is your name? : '),
print "Hello %s" % NAME
HOURS = raw_input('How many hours have you worked? :')
GROSS_PAY = (int(HOURS) * 10)
print "Having worked %s hours, at a rate of 10 pounds per hour you are\
 owed %s pounds." % (HOURS, GROSS_PAY),
print "Good-bye, and GOOD LUCK!"
