'''This is EX14's exercise file'''
from sys import argv

SCRIPT = argv
PROMPT = '<--->>> '

print "Hello, what is your name, please?"
USER_NAME1 = raw_input(PROMPT)
print "Hi %s, I'm the %r script." % (USER_NAME1, SCRIPT)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % USER_NAME1
LIKES = raw_input(PROMPT)

print "Where do you live, %s?" % USER_NAME1
LIVES = raw_input(PROMPT)

print "What kind of computer do you have, %s?" % USER_NAME1
COMPUTER = raw_input(PROMPT)

print "What's your favourite meal, ever %s" % USER_NAME1
MEAL = raw_input(PROMPT)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is or how to get there.
What's more, you have a %r computer, and you like to eat %r. Nice!
""" % (LIKES, LIVES, COMPUTER, MEAL)

print """
What's also interesting is that I can output all of the variables one
after the other, in sequence. See?
%r, %r, %r, %r, %r
""" % (USER_NAME1, LIKES, LIVES, COMPUTER, MEAL)
