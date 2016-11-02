from pint import UnitRegistry
ureg = UnitRegistry()

name = 'Frank'
age = 38 #Not a lie, it really is.
height = 188 #cm
weight = 80 #kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'  

print "Let's talk about %s." % name
print "He's %d cms tall." % height
print "He's %d kgs heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This is a tricky line:
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)
