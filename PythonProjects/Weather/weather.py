from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import requests
import sys

def initialize_scrape():

    #Note: Don't delete these two lines. 
    #https://stackoverflow.com/a/63573649
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    #header, so my ip doesn't get blocked
    scrape= requests.Session()
    scrape.auth = ('user', 'pass')
    scrape.headers.update({'x-test': 'true'})

    #def initialize_scrape():
        
    data=requests.get("https://weather.com/weather/tenday/l/4181a4e0dcf012d6922f701deb6abaf20c2f76aef5df5e06578aafc3833b73ef#detailIndex5")

    scrape=BeautifulSoup(data.content, "html.parser")

    #print(scrape.prettify)
    ######################
    #Works: prints weekday (sat sun etc) and numerical date (25, 26, etc)
    #ten_day=scrape.findAll(class_="DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF")
    #period=[]
    #for day in range(len(ten_day)):
    #    for iter in ten_day[day]:
    #        period.append(iter.find(class_="DetailsSummary--daypartName--1Mebr").get_text())
    #tonight=ten_day[0]
    #print(period[0])
    ############################

    ten_day=scrape.findAll(class_="DaypartDetails--DetailSummaryContent--1c28m Disclosure--SummaryDefault--1z_mF")
    #print(ten_day[0].prettify())

 

    get_day2=scrape.select(".DetailsSummary--daypartName--1Mebr")
    date=[day.get_text() for day in get_day2]
    #equivalent to top
    #for day in get_day2:
    #    x.append(day.get_text())
    #print(get_day2)

    #print("date: ", date)

    #get low/hightemp for day
    get_temp_low=scrape.select(".DetailsSummary--highTempValue--3x6cL")
    temp_low=[low.get_text() for low in get_temp_low]
    get_temp_high=scrape.select(".DetailsSummary--lowTempValue--1DlJK")
    temp_high=[high.get_text() for high in get_temp_high]

    #print("low: ", temp_low)
    #print("high: ",temp_high)

    #row
    #table=[
    #    ["Temp High: ", temp_high[0], temp_high[1],temp_high[2],temp_high[3],temp_high[4],temp_high[5],temp_high[6],temp_high[7]
    #    ,temp_high[8],temp_high[9],temp_high[10],temp_high[11],temp_high[12],temp_high[13]],
    #    ["Low Temp: ", temp_low[0], temp_low[1],temp_low[2],temp_low[3],temp_low[4],temp_low[5],temp_low[6],temp_low[7]
    #    ,temp_low[8],temp_low[9],temp_low[10],temp_low[11],temp_low[12],temp_low[13]]
    #    ]

    #column
    #print(tabulate(table,headers=["Day",date[0], date[1], date[2], date[3],date[4],date[5], date[6], date[7], date[8], date[9], date[10], date[11], date[12], date[13]],
    #    disable_numparse=True))
    
    return date, temp_high, temp_low
