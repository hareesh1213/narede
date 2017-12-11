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
import MySQLdb
#%%
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)


browser.open('https://www.netflix.com/tr/login')
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

#Mysql connection
db = MySQLdb.connect(host="localhost",user="root",passwd="N166i124Mbh",db="movies_scrap")
cur = db.cursor()

lists = [[] for i in range(10)]
for j in info.links:
    url = 'https://www.netflix.com' + str(j)
    browser.open(url)
    soup = BeautifulSoup(browser.response().read(), 'html5lib')
  
    lists[0].append(j)
    
    ##For CSV generation.
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

    ##For Mysql insertion.
    Movie_title = soup.find(class_='spotlight-name spotlight-readable').text.encode("utf-8")
    Thumb_urls  = soup.find(class_='spotlight-still spotlight-background-fill')['src']
    Video_urls  = 'https://www.netflix.com'+j
    Release_year =  soup.find(class_='spotlight-year').text+'-01-01'
    Vendor_id = 3
    created_date = time.strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""SELECT auto_id FROM tbl_movies WHERE title LIKE %s""", [Movie_title])
    movie_set = cur.fetchall()
    if(movie_set):
        for row in movie_set:
            movie_id = row[0]
            sql = "SELECT auto_id FROM tbl_prices WHERE movie_id = %s AND vendor_id = %s"% (movie_id,Vendor_id) 
            cur.execute(sql)
            price_set = cur.fetchall()
            if(price_set):
                cur.execute ("UPDATE tbl_prices SET video_url=%s, unique_id=%s, Rent_sd_price=%s, Rent_hd_price=%s, Buy_sd_price=%s, Buy_hd_price=%s, updated_date=%s  WHERE movie_id=%s AND vendor_id=%s", (Video_urls,'0',0,0,0,0,'1',created_date,movie_id,Vendor_id))
                #print cur._last_executed
            else:
                insert_sql = "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,is_subscribe,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(insert_sql,(movie_id,Video_urls,'0',Vendor_id,0,0,0,0,'1',created_date,created_date))
    else:
        ##Inserting into movies table
        if(Movie_title): 
            insert_sql1 =  "INSERT INTO tbl_movies (title,thumbnail_url,release_year) VALUES(%s,%s,%s)"
            cur.execute(insert_sql1,(Movie_title,Thumb_urls,Release_year))
            movie_id    = cur.lastrowid
            ##Inserting into prices table (need to update but_price,buyhd_price)
            insert_sql2 =  "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,is_subscribe,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(insert_sql2,(movie_id,Video_urls,'0',Vendor_id,0,0,0,0,'1',created_date,created_date))

    time.sleep(np.random.randint(2, 5))

info2 = pd.DataFrame(np.array(lists).T.tolist())
info3 = pd.merge(info2, info, how='inner', left_on=0, right_on='links')
#info3.to_csv('t11_out.csv', encoding='utf-8')
db.commit()
browser.close() 

