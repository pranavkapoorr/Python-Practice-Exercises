'''
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the Google homepage.
'''
import requests
from bs4 import BeautifulSoup

def getGoogleTitles(strng):
    url = 'http://google.com/search?q='+strng
    r = requests.get(url)
    r_html = r.text
    
    soup = BeautifulSoup(r_html,"lxml")
    titles = soup.find_all('h3', 'r')
    titleList = []
    for title in titles:
        title = "<html><body>"+ str(title) +"<html><body>"
        #print(title)
        val = BeautifulSoup(title,"lxml")
        titleList.append(str(val.find("b")).replace("<b>","").replace("</b>",""))
    return titleList
    
print(getGoogleTitles("python"))