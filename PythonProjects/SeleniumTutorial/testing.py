from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import requests
import sys
import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
# Keys class provide keys in the keyboard like RETURN, F1, ALT etc.

#Inheriting from TestCase class from unittest
class PythonOrgSearch(unittest.TestCase):
    #setUp is part of initialization, called before other functions
    #creating instance of chromedriver
    def setUp(self):
        options = Options()
        #headless means terminal, no ide used
        options.add_argument("--headless")
        
        self.driver = webdriver.Chrome(options=options)
        
        #if you dont want headless
        #self.driver=webdriver.Chrome()
        
    #important, tests must begn with "test" keyword like in Jest    
    def test_search_in_python_org(self):

        driver = self.driver

        # driver navigates to page
        driver.get("http://www.python.org")

        # aasserts that Python is in the title of the webpage
        assert "Python" in driver.title
        # we're finding an element by the name q
        elem = driver.find_element_by_name("q")

        # clearing any prepopulated text in the input fields
        elem.clear()

        # sending specific text/keys, keys==keyboard keys,
        elem.send_keys("pycon")
        # return=="enter" button
        elem.send_keys(Keys.RETURN)

        # If the assert above is false, and the title isn't what is written, then it does an error and prints it saying not found
        assert "No results found." not in driver.page_source
        
        #called after every test method.
        #clean up actions, in our case we quit browser
        def tearDown(self):
            self.driver.quit()
    
    
if __name__ == "__main__":
    #boiler plate code to run test suite
    unittest.main()