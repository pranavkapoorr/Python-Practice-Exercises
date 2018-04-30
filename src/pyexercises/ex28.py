'''
Implement a function that takes as input three variables, 
and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. 
All you need is some variables and if statements!
'''
def getLargest(v1,v2,v3):
    if v1 > v2  and  v1 > v3 :
        return v1
    elif v2 > v1 and v2 > v3 :
        return v2
    elif v3 > v1 and v3 > v2 :
        return v3
    
print(getLargest(5 , 6 , 10))