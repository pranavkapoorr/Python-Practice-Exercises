'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

-If the number is a multiple of 4, print out a different message.
-Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
number = int(input("please enter the number : "))
if number % 2 == 0:
    if number % 4 == 0:
        print("entered number "+ str(number) +" is multiple of 4 and 2")
    else:
        print("entered number "+ str(number) +" is even")
else:
    print("entered number "+ str(number) +" is odd")
    


number = int(input("please enter the number : "))
divisor = int(input("please enter the divisor : "))
if number % divisor == 0:
    if (number / divisor) % 2 == 0:
        print("entered number "+ str(number) +" is evenly divided by "+str(divisor))
    else:
        print("entered number "+ str(number) +" is not evenly divided by "+str(divisor))
else:
    print("entered number "+ str(number) +" is not a multiple of "+str(divisor))