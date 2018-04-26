'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that cannot be divided by any other number. 
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
The explanation is easier with an example, which I will describe below.)
'''
def readFromFileAsList(fileName):
    listX = []
    fileX = open(fileName + '.txt', 'r')
    while fileX.readline():
        line = fileX.readline().strip()
        listX.append(line)
    fileX.close()
    return listX    

primeNumbers = readFromFileAsList("resources/ex23/One")
happyNumbers = readFromFileAsList("resources/ex23/Other")

overlappingNumbers = [n for n in primeNumbers if n in happyNumbers]
print(overlappingNumbers)