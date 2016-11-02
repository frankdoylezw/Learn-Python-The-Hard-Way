#DEFINING X variable and assigning it an integer value of 10. %d is the string format for integer.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#Assigning a string value to y. %s is the string format converter. NB the % after the closing ", but before the variables are listed.
y= "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r means 'print exactly this'.Because you have already assigned x, it simply prints it out with assigned variables in place
print "I said: %r." % x

#Similar to the above %s simply converts y to a string and displays it.
print "I also said: '%s'." % y

#This is a Boolean
hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#Using the + symbol means that the lines are shown concatenated.
print w + e
