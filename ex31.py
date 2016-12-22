#!/usr/bin/env python

"""Exercise 31. Nested IF statements"""
import webbrowser
import sys
from os import system
import os
import time


system('clear')

def main():
    print "Enter your name: "
    NAME = raw_input("> ")
    print "Welcome " + NAME + ", nice to have you round these parts."

    print "\nYou enter a dark room with three doors. Do you go through DOOR #1, DOOR #2, DOOR #3?"

    DOOR = raw_input("> ")

    if DOOR == "1":
        print "\nThere's a giant BEAR here, eating cheesecake. What do you do?"
        print "\n1. Take the cake."
        print "\n2. Scream at the bear."
        print "\n3. Pull down your pants and moon the bear."

        BEAR = raw_input("> ")

        if BEAR == "1":
            print "\nThe bear eats your face off. Good job!"
        elif BEAR == "2":
            print "\nThe bear eats your legs off. Good job!"
        elif BEAR == "3":
            print "\nMOONING A BEAR??! WTF????! He snacks on your ass. Soz."
        else:
            print "\nWell, doing %s is probably better. The bear runs away." % BEAR

    elif DOOR == "2":
        print "\nYou stare into the endless abyss at Cthulhu's retina."
        print "\n1. Blueberries."
        print "\n2. Yellow jacket clothespins."
        print "\n3. Understanding revolvers yelling melodies."

        INSANITY = raw_input("> ")

        if INSANITY == "1" or INSANITY == "2":
            print "Your body survives powered by a mind of jello. Good job!"
        else:
            print "The insanity rots your eyes into a pool of muck. Good job!"

    elif DOOR == "3":
        print "\nYou see Silvio Berlusconi wearing nothing but a toga. What do you do, Soldier?"
        print "\n1. Kick him in the nuts and run!"
        print "\n2. Say 'Nice toga, Silvio!' and run!"
        print "\n3. Join Silvio for the evening's fun."

        SILVIO = raw_input("> ")

        if SILVIO == "1":
            print "\nGood option. The guy always was a greaseball.\n"
        elif SILVIO == "2":
            print "\nPolite and wise - a rare combo, well done.\n"
        elif SILVIO == "3":
            print "\nYou're a scabby lowlife, you know that?\n"
        else:
            print "\nYeah, you're right. No option was really you."
    else:
        print "\nYou stumble around and fall on a knife and die. Shit luck."

main()

print "Game Over. Do you want to play again? (y/n)"
AGAIN = raw_input("> ")

if AGAIN == "y":
    os.execv(sys.executable, ['python'] + sys.argv)

else:
    print "Goodbye, Sucker."
    time.sleep(2)
    webbrowser.open_new('https://thesuperjesus.files.wordpress.com/2008/04/fail.jpg')
