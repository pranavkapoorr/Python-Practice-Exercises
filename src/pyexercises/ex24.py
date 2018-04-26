# coding: iso-8859-1
'''
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.
'''
def horizontal(size):
    strng = ""
    for i in range(size):
        strng = strng + (" ---")      
    return strng
def vertical(size):
    strng = ""
    for i in range(size):
        strng = strng + ("|   ")      
    return strng
def createGameBoard(size):
    strng = ""
    strng = strng + horizontal(size) +"\n"+vertical(size+1) + "\n" + horizontal(size) + "\n"
    return strng

print(createGameBoard(3))