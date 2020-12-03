from weather import *
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import requests
import time

def init():
    day, high, low=initialize_scrape()  
    table=[
            ["Temp High (C): ", high[0], high[1],high[2],high[3],high[4],high[5],high[6],high[7]
            ,high[8],high[9],high[10],high[11],high[12],high[13]],
            ["Low Temp (C): ", low[0], low[1],low[2],low[3],low[4],low[5],low[6],low[7]
            ,low[8],low[9],low[10],low[11],low[12],low[13]]
            ]
     
    print(tabulate(table,headers=["Day",day[0], day[1], day[2], day[3],day[4],day[5], day[6], day[7], day[8], day[9], day[10], day[11], day[12], day[13]],
            disable_numparse=True), "\n \n")

def main():
    
    while True:
       #wait 3.20 minutes before prining results
        l=init()
        time.sleep(200) 
    
main()