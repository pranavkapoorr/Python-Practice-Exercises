'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

-Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
-Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
name = input("input your name please!: ")
age = input("input your age please: ")
toPrint = "name - "+ name + " age - "+ age + "\n"
import datetime
now = datetime.datetime.now()
print("you ll be 100 years old in : "+ str(int(now.year)+(100-int(age))))


times = int(input("enter a number to print you name that many times: "))
print(times * toPrint)

