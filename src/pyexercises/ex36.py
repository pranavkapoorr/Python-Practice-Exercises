# coding: iso-8859-1
'''
This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.
In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! 
Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. 
Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.
If you are using a purely web-based interface for coding, this exercise won’t work for you, since it requires installing the bokeh Python package. 
Now might be a good time to install Python on your own computer.
'''
import json
from collections import Counter

def showOnGraph(x,y):
    from bokeh.plotting import figure, show, output_file
    # we specify an HTML file where the output will go
    output_file("plot.html")
    print(x)
    print(y)
    # load our x and y data
    x = x
    y = y
    # create a figure
    p = figure(x_range=x)
    # create a histogram
    p.vbar(x=x, top=y, width=0.2)
    # render (show) the plot
    show(p)

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
print(months)
allMonths = list(num_to_string.values())
dicX = {}
for m in allMonths:
    for m1 in months:
        if m == m1:
            if m in dicX.keys():
                print(m,m1)
                dicX[m] += 1
            else:
                dicX[m] = 1
        else:
            dicX[m] = 0
    
showOnGraph(list(dicX.keys()), list(dicX.values()))


