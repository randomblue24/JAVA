from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd
#requests api
import requests

#requests teh page, and gets the status code, and stores it in page
#request library makes a get request to web server, which will download HTML content of page
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

#print(page)

#prints status code from get request
print(page.status_code)

#print out HTML content of page
print(page.content)

#using beautifulSoup to parse document and esxtract text from p tag. 
soup = BeautifulSoup(page.content, 'html.parser')

#print formatted html page using prettify on BeautifulSoup object
print(soup.prettify())

#more through structure 1 lvl at a time. Select top lvl elements using
#children property, returns list generator, call list function
x=list(soup.children)

print(x)

#prints type of eah element in list
print([type(item) for item in list(soup.children)])

#select html tag +children, by taking 3rd item in list
print("\n")
#select html tag +children, by taking 3rd item in list
html=list(soup.children)[2]
print(html)
print("\n")

#extracting 3rd element in list of html, to select p tag
body=list(html.children)[3]

p=list(body.children)
print (p)

p=list(body.children)[1]
print(p)

print("\n")

#use get_text() to extract text from tag
text=p.get_text()
print(text, "\n")

###############################################
#Top code is good fr page naviagtion
#Finding all instances of a tag
#use .find_all() - returns list of all p elements + info, lopp through
print("all paragraphs")
soup = BeautifulSoup(page.content, 'html.parser')
all_p=soup.find_all('p')
print(all_p, '\n')

all_p=soup.find_all('p')[0].get_text()
print(all_p)