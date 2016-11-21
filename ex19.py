"""Exercise 19 files
"""
#Here, I'm clearing the screen before the bulk of the script is run
import os
os.system('clear')

"""Here, we write our function. It's called
cheese_and_crackers. It simply prints out what you give it as values
for the cheeses and boxes of crackers, whether directly, by variables,
by maths inside the arguments, or by variables & maths combined"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """This functions prints out amounts of cheese and crackers"""
    print "You have %d cheeses!" % (cheese_count)
    print "You have %d boxes of crackers!" % (boxes_of_crackers)
    print "Man, that's enough for a party!!"
    print "Get WASTED, BRU! \n"

"""Here we call the function, and just give it two numbers to work with
"""
print "We can just give the function numbers directly: "
cheese_and_crackers(10, 20)

"""Here we pass in variables as the arguments. NOTE: the variable names
ARE NOT the same as the arguments in the function definition. 
"""
print "\nOr, we can use variables: "
AMOUNT_OF_CHEESE = 10
AMOUNT_OF_CRACKERS = 50
cheese_and_crackers(AMOUNT_OF_CHEESE, AMOUNT_OF_CRACKERS)

print "\nWe can even do maths inside, too!"
cheese_and_crackers(10+55, 5+6)

print "\nAnd we can combine the two, variables and maths!"
cheese_and_crackers(AMOUNT_OF_CHEESE + 10, AMOUNT_OF_CRACKERS -1)

