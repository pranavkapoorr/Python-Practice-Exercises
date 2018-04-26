# coding: iso-8859-1
'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 
I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above 
(or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. 
This text file is actually a list of files corresponding to the SUN database scene recognition database, 
and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, 
it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. 
I talked a little bit about it in this post.
'''

def readFromFile1(fileName):
    dic = {}
    fileX = open(fileName + '.txt', 'r')
    while fileX.readline():
        line = fileX.readline().strip()
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1
    fileX.close()
    return dic

print(readFromFile1("resources/ex22/namelist"))


def readFromFile2(fileName):
    dic = {}
    filex = open(fileName + '.txt', 'r')
    while filex.readline():
        line = filex.readline().strip()[3:-25]
        if line in dic:
            dic[line] += 1
        else:
            dic[line] = 1
    filex.close()
    return dic

print(readFromFile2("resources/ex22/training_01"))


