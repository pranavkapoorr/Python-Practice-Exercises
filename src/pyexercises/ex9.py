# coding: iso-8859-1
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random
guesses = 0
num = random.randint(1,9)
while True:
    unum = int(input("make your guess between 1 and 9 : "))
    guesses += 1
    if unum > num :
        print("your guess "+ str(unum) +" is higher than number "+str(num))
    elif unum < num :
        print("your guess "+ str(unum) +" is lower than number  "+str(num))
    elif unum == num :
        print("your guess is RIGHT...." +str(num) +" == "+ str(unum) +" guesses = "+ str(guesses) )
        break