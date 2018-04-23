'''
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import random
import string

def generatePassword(size):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for _ in range(size))

print(generatePassword(int(input("How many characters in password ?: "))))