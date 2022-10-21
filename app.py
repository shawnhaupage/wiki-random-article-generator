#!/usr/bin/env python3
from types import NoneType
import requests, re
from bs4 import BeautifulSoup as bs4
import webbrowser

#Header to avoid web scraping detection
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'}

#Wikipedia auto-generate random article
url = 'https://en.wikipedia.org/wiki/Special:Random'

def generate_random_WIKI():

    #Pull article content
    response = requests.get(url, headers=headers)
    soup = bs4(response.content, 'html.parser')

    #If the 'Title' tag does not exist, try a new article
    try:
        title = soup.find(class_='mw-page-title-main').text
    except:
        generate_random_WIKI()

    URL_title = str(re.sub(' ','_',title))
    print('Title: ' + title)
    ans = input('Do you want to view this article? (Y/N): ')
    if ans == 'Y' or ans == 'y':
        print('Okay! Opening URL...')
        open_url = 'https://en.wikipedia.org/wiki/' + URL_title
        webbrowser.open(open_url)
    elif ans == 'N' or ans == 'n':
        generate_random_WIKI()
    else:
        'Must type Y or N'
        generate_random_WIKI()

generate_random_WIKI()