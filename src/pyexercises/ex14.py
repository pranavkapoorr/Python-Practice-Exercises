'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def removeDuplicatesWithoutSet(listX):
    temp = []
    for e in listX:
        if e not in temp:
            temp.append(e)
    return temp

def removeDuplicatesWithSet(listX):
    return list(set(listX))


print(removeDuplicatesWithoutSet(a))
print(removeDuplicatesWithSet(a))