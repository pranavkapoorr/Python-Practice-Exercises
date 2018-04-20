# coding: iso-8859-1
'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''
def fibonacci(num):
    li = []
    temp = 0
    num1 = 1
    num2 = 1
    if num == 1:
        li.append(num1)
    elif num ==2:
        li.append(num1)
        li.append(num2)
    if num>2:
        li.append(num1)
        li.append(num2)
        for x in range(0,num-2):
            temp = num1 + num2
            num1 = num2
            num2 = temp
            li.append(temp)

    return li


print(fibonacci(2))