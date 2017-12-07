# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log  
from twisted.enterprise import adbapi  
from scrapy.http import Request  
from scrapy.exceptions import DropItem  
#from scrapy.contrib.pipeline.images import ImagesPipeline  
import time  
#import psycopg2
import MySQLdb 


class GooglescrapPipeline(object):  
  
    def __init__(self):  
        #Mysql Database connection.
        self.conn = MySQLdb.connect("localhost","root","N166i124Mbh","movies_scrap")

        
    def process_item(self, item, spider):
            #If crawler is from google play movies
            created_date = time.strftime("%Y-%m-%d %H:%M:%S")
            cur          = self.conn.cursor() 
            if(item and spider.name == 'playcrawler'):
              Vendor_id = 1 

              if(item["Rent_sd_price"]==0):
                  item["Rent_sd_price"] = item["Rent_price"]
              if(item["Buy_sd_price"]==0):
                  item["Buy_sd_price"] = item["Buy_price"]
              ##Inserting into movies table
              cur.execute("INSERT INTO tbl_movies (title,description,thumbnail_url,video_url,unique_id,vendor_id,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(item["Movie_title"],'',item["Thumb_urls"],item["Video_urls"],item["Unique_id"],Vendor_id,created_date,created_date))
              movie_id    = cur.lastrowid
              ##Inserting into prices table (need to update but_price,buyhd_price)
              cur.execute("INSERT INTO tbl_prices (movie_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(movie_id,Vendor_id,item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"], created_date,created_date))
              self.conn.commit()
            #If crawler is from Itunes movies
            
            return item

        
