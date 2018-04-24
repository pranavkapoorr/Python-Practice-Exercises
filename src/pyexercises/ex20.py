'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
'''
def isPresent(randset,usrnum):
    start_index = 0
    end_index = len(randset) - 1
    while True:
        middle_index = int((end_index + start_index) / 2)
        middle_element = randset[middle_index]
        if middle_element == usrnum or randset[start_index]==usrnum or randset[end_index]==usrnum:
            return True
            break
        if middle_index == start_index or middle_index == end_index or middle_index == 0:
            return False
            break
        elif middle_element > usrnum:
            end_index = middle_index
        else:
            start_index = middle_index

a = [1, 3, 5, 30, 42, 43, 500]

print(isPresent(a, 9))