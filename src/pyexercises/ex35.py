# coding: iso-8859-1
'''
This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, 
load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
    "May": 3,
    "November": 2,
    "December": 1
}
'''
import json
from collections import Counter

with open("resources/ex34/birthdays.json", "r") as f:
    birthdays = json.load(f)

num_to_string = {
    1: "January",
    2: "February",
    3: "March", 
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

months = []
print(birthdays)
for name, birthday_string in birthdays.items():
    print(name,birthday_string)
    month = int(birthday_string.split("/")[1])
    months.append(num_to_string[month])

print(Counter(months))