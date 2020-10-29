from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import requests
import sys

#Note: Don't delete these two lines. 
#https://stackoverflow.com/a/63573649
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

########################################################################
#r = requests.get('https://www.youtube.com/playlist?list=PL3D7BFF1DDBDAAFE5')
#page = r.text
#soup=bs(page,'html.parser')
#res=soup.find_all('a',{'class':'pl-video-title-link'})
#for l in res:
#    print l.get("href")


utube = requests.Session()
utube.auth = ('user', 'pass')
utube.headers.update({'x-test': 'true'})


#scraping youtube
utube=requests.get("https://www.youtube.com/playlist?list=PL7WPPJyySU9gDZAFLRXHi2B1lCYpmaAX9")
array=utube[0]

print(array)