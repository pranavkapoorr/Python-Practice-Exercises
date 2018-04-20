'''
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''
def giveFirstAndLast(listX):
    return [listX[0],listX[-1]]

a = [5, 10, 15, 20, 25]
myList = giveFirstAndLast(a)
print(myList)
