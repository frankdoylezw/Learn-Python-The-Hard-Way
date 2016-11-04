#This is the coolest exercise, yet
#It takes input from the user

print "How old are you?",

#raw_iput is a python function that waits for and then uses user input
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)