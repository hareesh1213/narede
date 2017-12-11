# -*- coding: utf-8 -*-
"""
Created on Tue May 03 20:52:22 2016

@author: Mayank Kapoor
"""
#import requests
import pandas as pd
import time
from time import gmtime, strftime
import mechanize
import re
from bs4 import BeautifulSoup
import numpy as np
#%%
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)


browser.open('https://www.netflix.com/tr-en/login')
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
#username/email and pass below
browser.form['email'] = 'guclutalu@smartup.network'
browser.form['password'] = 'Smartnet9291'
response = browser.submit()
#print response.read()

#%%
#get all links of turkish shows and movies
browser.open('https://www.netflix.com/search?q=turkish')
links = list(browser.links())

soup_main = BeautifulSoup(browser.response().read(), 'html5lib')

#reference
info = pd.DataFrame()
info['posters'] = soup_main.find_all(class_='title-boxart')
info['links'] = [i['data-href'] for i in soup_main.find_all(class_='watch-page-link')]
info['raw_info'] = list(soup_main.find_all(class_='watch-page-link'))


#helper function
def try_except(x, list):
    try:
        return(x)
    except:
        return(list.append(np.nan))

#%%
lists = [[] for i in range(10)]
for j in info.links:
    url = 'https://www.netflix.com' + str(j)
    browser.open(url)
    soup = BeautifulSoup(browser.response().read(), 'html5lib')
  
    lists[0].append(j)
    
    try_except(lists[1].append(soup.find(class_='spotlight-name spotlight-readable').text), lists[1])
    try_except(lists[2].append(soup.find(class_='spotlight-description spotlight-readable').text), lists[2])
    try_except(lists[3].append(soup.find(class_='spotlight-maturity').text), lists[3])
    try_except(lists[4].append(soup.find(class_='spotlight-duration').text), lists[4])
    try_except(lists[5].append(soup.find(class_='spotlight-year').text), lists[5])
    try_except(lists[6].append(', '.join([i.text for i in soup.find_all(class_='person-section') if re.findall('person', str(i))])), lists[6])
    try_except(lists[7].append(', '.join([i.text for i in soup.find_all(class_='details-link') if re.findall('person', str(i))])), lists[7])
    try_except(lists[8].append(str([i.text for i in soup.find_all(class_='details-link') if re.findall('genre', str(i))])), lists[7])
    try_except(lists[9].append(str(soup.find(class_='spotlight-still spotlight-background-fill')['src'])), lists[9])
    print(j)
    time.sleep(np.random.randint(2, 5))



info2 = pd.DataFrame(np.array(lists).T.tolist())
info3 = pd.merge(info2, info, how='inner', left_on=0, right_on='links')
info3.to_csv('t11_out.csv', encoding='utf-8')
#browser.close()
