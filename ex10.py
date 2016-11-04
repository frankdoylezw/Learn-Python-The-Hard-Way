#We're declaring a load of variables up here at the top, again.
#In this first line, we see the tabbing escape character.
tabby_cat = "\tI'm tabbed in."
#In the next line we see the new line escape character
persian_cat = "I'm split \non a line"
#Here we see the ability to still include a slash in the text, by escaping with another slash
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\r
\r
\r

\t\tYO YO YO
\v
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat