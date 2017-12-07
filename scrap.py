from bs4 import BeautifulSoup
from warnings import filterwarnings

import urllib2
import MySQLdb
import time
import re


global_url = "https://play.google.com"
db	   = MySQLdb.connect("localhost","root","","movies_scrap_data")
cursor = db.cursor()


source 	= "https://play.google.com/store/movies"
page 	= urllib2.urlopen(source)
soup 	= BeautifulSoup(page, "html.parser")
movie_datalist = soup.findAll("div",{"class": "card no-rationale tall-cover movies small"})
created_date = time.strftime("%Y-%m-%d %H:%M:%S")
vendor_id = 1
rowcount  =	0

for movie_data in movie_datalist:
    #print global_url+a['href']
    thumb_url_data 		= movie_data.find('img', {'class': 'cover-image'})
    thumb_urls 			= thumb_url_data.get('src')

    video_url_data 		= movie_data.find('a', {'class': 'card-click-target'})
    video_urls 			= global_url+video_url_data.get('href')

    movie_title_data	= movie_data.find('a', {'class': 'title'})
    movie_title 		= movie_title_data.text

    movie_price_data 	= movie_data.find('span', {'class': 'display-price'})
    movie_price 		= re.search(r'\d+',movie_price_data.text)
    numeric_movie_price = movie_price.group()

    unique_id 			= movie_data.find('div', {'class': 'card-content id-track-click id-track-impression'})['data-docid']
    
    '''Inserting into movies table'''
    cursor.execute("INSERT INTO tbl_movies (title,description,thumbnail_url,video_url,unique_id,vendor_id,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(movie_title,'',thumb_urls,video_urls,unique_id,vendor_id,created_date,created_date))
    movie_id 		=	cursor.lastrowid
    
    '''Inserting into prices table'''
    cursor.execute("INSERT INTO tbl_prices (movie_id,vendor_id,price_value,created_date,updated_date) VALUES(%s,%s,%s,%s,%s)",(movie_id,vendor_id,numeric_movie_price,created_date,created_date))
    rowcount += 1
print("Inserted Movies = {}".format(rowcount))

db.commit()