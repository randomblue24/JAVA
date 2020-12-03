from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import requests
import sys
import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#Keys class provide keys in the keyboard like RETURN, F1, ALT etc.

options = Options()
#This allows us to not have the selenium IDE open, and just use it via terminal
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

#driver navigates to page
driver.get("http://www.python.org")

#aasserts that Python is in the title of the webpage
assert "Python" in driver.title
#we're finding an element by the name q
elem = driver.find_element_by_name("q")

#clearing any prepopulated text in the input fields
elem.clear()

#sending specific text/keys, keys==keyboard keys, 
elem.send_keys("pycon")
#return=="enter" button
elem.send_keys(Keys.RETURN)

#If the assert above is false, and the title isn't what is written, then it does an error and prints it saying not found
assert "No results found." not in driver.page_source

print(driver)

driver.quit()


