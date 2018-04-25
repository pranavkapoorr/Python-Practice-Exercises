# coding: iso-8859-1
'''
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, 
use the code from the solution), and instead of printing the results to a screen, 
write the results to a txt file. In your code, 
just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
'''
def writeToFile(fileName , textToWrite):
    file = open(fileName + '.txt', 'w')
    file.write(textToWrite)
    file.close()
    print("Successfully Written to file!")

content = "Hi there, I am new text file generated using Python ... !"
writeToFile(input("give file name please: "),content)
