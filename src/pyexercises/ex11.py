'''
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
 described below.
'''

def isNotPrime(num):
    result = False;
    for i in range(2,num) :
        if  num % i == 0 :
            result = True
    return result
    
num = int(input("enter the number please : "))
        
if isNotPrime(num):
    print("number "+ str(num) + " is not prime")
else:
    print("number "+ str(num) + " is prime")
