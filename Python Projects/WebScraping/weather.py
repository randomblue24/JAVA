# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

# requests api
import requests

page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
)

soup = BeautifulSoup(page.content, "html.parser")
# extracting data from extended weather

# using find, to find the 1st instance of the specified id
seven_day = soup.find(id="seven-day-forecast")

# from the var seven day that stores all the seven day forecasts
# we're finding ALL instances of tombstone container, because that's
# where the forecast for each day is stored
forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]

print(tonight.prettify())

print("\n")

###################################################################

# Extracting info

# extracting name of forecast item, short-description, and temp
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

# Extracting Title from img tag, it's a description of weather
img=tonight.find("img")
desc=img['title']
print(desc)

print("\n 1")
##############################################################

#Extracting ALL info from page
#using html+css selectors

period_tags=seven_day.select(".tombstone-container .period-name")
periods=[pt.get_text() for pt in period_tags]

print(periods)
      
print('\n 2')

short_desc=[sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps=[t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs=[d["title"] for d in seven_day.select(".tombstone-container img")]

#print("periods: ", periods)
#print(short_desc)
#print("temps:", temps)
#print(descs)
print('\n')
#print(temp)
#rows
weather_table=[
    temps[0],
    temps[1],
    temps[2],
    temps[3],
    temps[4],
    temps[5],
    temps[6],
    temps[7],
    temps[8],
    ],
#columns
print(tabulate(weather_table,headers=[periods[0],periods[1],periods[2], periods[3],periods[4], periods[5], periods[6], periods[7], periods[8]],
                   disable_numparse=True))
    

