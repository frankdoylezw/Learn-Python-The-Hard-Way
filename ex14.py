'''This is EX14's exercise file'''
from sys import argv

SCRIPT, USER_NAME = argv
PROMPT = '>> '

print "Hi %s, I'm the %s script." % (USER_NAME, SCRIPT)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % USER_NAME
LIKES = raw_input(PROMPT)

print "Where do you live, %s?" % USER_NAME
LIVES = raw_input(PROMPT)

print "What kind of computer do you have, %s?" % USER_NAME
COMPUTER = raw_input(PROMPT)

print "What's your favourite meal, ever %s" % USER_NAME
MEAL = raw_input(PROMPT)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is or how to get there.
What's more, you have a %r computer, and you like to eat %r. Nice!
""" % (LIKES, LIVES, COMPUTER, MEAL)

print """
What's also interesting is that I can output all of the variables one
after the other, in sequence. See?
%r, %r, %r, %r
""" % (LIKES, LIVES, COMPUTER, MEAL)
