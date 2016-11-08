#!/usr/bin/python
# Version 1
## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')
 
## Get input ###
CHOICE = raw_input('Enter your CHOICE [1-3] : ')
 
### Convert string to int type ##
CHOICE = int(CHOICE)
 
### Take action as per selected menu-option ###
if CHOICE == 1:
        print ("Starting backup...")
elif CHOICE == 2:
        print ("Starting user management...")
elif CHOICE == 3:
        print ("Rebooting the server...")
else:    ## default ##
        print ("Invalid number. Try again...")