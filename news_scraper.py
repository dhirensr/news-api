import time
import re
import requests
from bs4 import BeautifulSoup

#Tracks how much time the script runs
#start = time.time()

# Creating soup objects in general
def make_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_ndtv_business_news(url):
    news_json = []
    soup = make_soup(url)
    all_headers = soup.find_all("h2",{"class" : "nstory_header"})
    for heading in all_headers:
        title = heading.a.text.strip()
        link = heading.a['href']
        news_json.append({'title': title, "url" : link , "source" : "NDTV Business"})

    return news_json


def get_livemint_news(url):
    news_json = []
    soup = make_soup(url)
    all_headers = soup.find_all("div",{"class" : "headlineSec"})
    for heading in all_headers:
        title = heading.a.text.strip()
        link = "https://www.livemint.com/" + heading.a['href']
        news_json.append({'title': title, "url" : link, "source" : "Livemint"})
    return news_json


def get_economic_times_news(url):
    news_json = []
    soup = make_soup(url)
    all_headers = soup.find_all("div",{"class" : "eachStory"})
    for heading in all_headers:
        title = heading.h3.a.text.strip()
        link = "https://economictimes.indiatimes.com" + heading.h3.a['href']
        news_json.append({'title': title, "url" : link, "source" : "Economic Times"})
    #print(news_json)
    return news_json

def get_business_standard_news(url):
    news_json = []
    soup = make_soup(url)
    all_headers = soup.find_all("div",{"class" : "listing-txt"})
    for heading in all_headers:
        #print(heading)
        title = heading.h2.a.text.strip()
        link = "https://www.business-standard.com" + heading.h2.a['href']
        news_json.append({'title': title, "url" : link, "source" : "Business Standard"})
    return news_json


def get_moneycontrol_news(url):
    news_json = []
    soup = make_soup(url)
    all_headers = soup.find_all("ul",{"id" : "cagetory"})[0].find_all("li")
    for heading in all_headers:
        if heading.a:
            title = heading.a['title']
            link = heading.a['href']
            news_json.append({'title': title, "url" : link, "source" : "Moneycontrol"})
    return news_json




#get_ndtv_business_news("https://www.ndtv.com/business/latest/")
#get_livemint_news("https://www.livemint.com/listing/subsection/market~stock-market-news/")
#get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146843&img=0&curpg=2")
#get_business_standard_news("https://www.business-standard.com/category/markets-ipos-news-1061101.htm")
#get_moneycontrol_news("https://www.moneycontrol.com/news/business/markets/")
# print ('\nAll done!')
# end = time.time()
# print ("\nTotal time for running:")
# print(end - start)
