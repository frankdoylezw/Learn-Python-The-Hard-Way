from os import system
from random import randint

system('clear')
frankslist = ['Volvo', 'Ferrari', 'Nazi', 'Mike']
print "This is the first list: "
print frankslist
frankslist.append('APPENDED')
print "This is the new list with the appended word: "
print frankslist
print ("Last item in the list ", frankslist.pop())
print frankslist
print "Number of items in the list after POP: ", len(frankslist)

#TESTING the RANGE function and a FOR LOOP:
testlistrange = []
for items in range(0, 6):
    print "Adding a new item to the list: %d" %items
    testlistrange.append(items)

for things in testlistrange:
    print " Thing is: %d" %things, "WOOOOHOOO!", randint(160000, 170000)


