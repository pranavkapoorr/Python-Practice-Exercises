# coding: iso-8859-1
'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

'''

num = int(input("please enter the number : "))
myList = []
for x in range(1,num):
    if num % x == 0:
        myList.append(x)

print(myList)