# coding: iso-8859-1
'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
stringToCheck = input("please enter the string: ")
if stringToCheck == stringToCheck[::-1]:
    print("entered string "+stringToCheck +" is palindrome")
else:
    print("entered string "+stringToCheck +" is NOT palindrome")