# coding: iso-8859-1
'''
This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.
In the previous exercise we created a dictionary of famous scientistsí birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, 
rather than having the dictionary defined in the program.
Bonus: Ask the user for another scientistís name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientistís name. 
If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.
'''
import json

birthday = {}
with open('resources/ex34/birthdays.json', 'r') as f:
        birthday = json.load(f)

def add_entry():
    name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
    date = input('When is {} born?\n'.format(name))
    birthday[name] = date
    with open('resources/ex34/birthdays.json', 'w') as f:
        json.dump(birthday, f)
        
    print('{} was added to my birthday list\n'.format(name))

def find_date():
    name = input("who's birthday do you want to know?\n").title()
    try :
        if birthday[name]:
            print('{} is born on {}\n'.format(name, birthday[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))

def list_entries():
    print('The current entries in my birthday list are:\n============================================')
    for key in birthday:
        print(key.ljust(31), ':', birthday[key])
    print()

while True:
    what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
    if what_next == 'Quit':
        print('Good Bye')
        raise SystemExit(0)
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_date()
    elif what_next == 'List':
        list_entries()