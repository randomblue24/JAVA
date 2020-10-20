#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd
#requests api
import requests


page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

#create beautifulsoup object, using it parse document. 
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify(), '\n')

#find all instances of the p tag with class "outer-text"
#note, cant seem to combine prettify with find_all, find_all only works with bs object
print(soup.find_all('p', class_='outer-text'))

print("\n")

#looking for any text with class "outer-text" which is all p tags
print(soup.find_all(class_="outer-text"))

print("\n")

#search for elements by id
print(soup.find_all(id="first"))

print("\n \n")

#################################################################
#Css selectors

#can use "select" to search for css elements

#using css selector to find p tags inside divs
#looking for p inside divs
print(soup.select("div p"))
