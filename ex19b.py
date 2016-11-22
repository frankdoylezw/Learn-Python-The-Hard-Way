"""
This is my own function
"""
import os
os.system('clear')


def tables_and_chairs(tables_count, chairs_count):
    print "There are 4 people per table"
    print "\nYou need %d tables and %d chairs" % (tables_count, chairs_count)
    print "\n"
ATTENDING = raw_input("How many people are attending this shindig? ")
print "Here are the number of tables and chairs you need:"
TABLES = (float(ATTENDING) //4)
CHAIRS = float(ATTENDING)
tables_and_chairs(TABLES, CHAIRS)
