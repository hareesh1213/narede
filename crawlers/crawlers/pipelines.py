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
import datetime,time  
#import psycopg2
import MySQLdb 


class CrawlersPipeline(object):  
  
    def __init__(self):  
        #Mysql Database connection.
        self.conn = MySQLdb.connect("localhost","root","N166i124Mbh","movies_scrap_new",charset="utf8", use_unicode=True) #N166i124Mbh  movies_scrap_data2

        
    def process_item(self, item, spider):
            #If crawler is from google play movies
            created_date = time.strftime("%Y-%m-%d %H:%M:%S")
            cur          = self.conn.cursor()

            ########START:: Google play movies ###############################################
            if(item and spider.name == 'googleplay'):
              Vendor_id = 1 

              if(item["Rent_sd_price"]==0):
                  item["Rent_sd_price"] = item["Rent_price"]
              if(item["Buy_sd_price"]==0):
                  item["Buy_sd_price"] = item["Buy_price"]
              #Check if movie already existed.
              movie_title = item['Movie_title']
              cur.execute("""SELECT auto_id FROM tbl_movies WHERE title LIKE %s""", [movie_title])
              movie_set = cur.fetchall()
              if(movie_set):
                for row in movie_set:
                    movie_id = row[0]
                    sql = "SELECT auto_id FROM tbl_prices WHERE movie_id = %s AND vendor_id = %s"% (movie_id,Vendor_id) 
                    cur.execute(sql)
                    price_set = cur.fetchall()
                    if(price_set):
                      cur.execute ("UPDATE tbl_prices SET video_url=%s, unique_id=%s, Rent_sd_price=%s, Rent_hd_price=%s, Buy_sd_price=%s, Buy_hd_price=%s, updated_date=%s  WHERE movie_id=%s AND vendor_id=%s", (item["Video_urls"],item["Unique_id"],item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"], created_date,movie_id,Vendor_id))
                      #print cur._last_executed
                    else:
                      insert_sql = "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                      cur.execute(insert_sql,(movie_id,item["Video_urls"],item["Unique_id"],Vendor_id,item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"], created_date,created_date))
              else:
                ##Inserting into movies table
                insert_sql1 =  "INSERT INTO tbl_movies (title,thumbnail_url,release_year) VALUES(%s,%s,%s)"
                cur.execute(insert_sql1,(item["Movie_title"],item["Thumb_urls"],item["Release_year"]))
                movie_id    = cur.lastrowid
                ##Inserting into prices table (need to update but_price,buyhd_price)
                insert_sql2 =  "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(insert_sql2,(movie_id,item["Video_urls"],item["Unique_id"],Vendor_id,item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"], created_date,created_date))
                
                self.conn.commit()
              return item
            ########END:: Google play movies ################################################

            ########START:: Itunes movies ###################################################   
            if(item and spider.name == 'itunes'):
              Vendor_id = 2

              '''if(item["Rent_sd_price"]==0):
                  item["Rent_sd_price"] = item["Rent_price"]'''
              if(item["Buy_sd_price"]==0):
                  item["Buy_sd_price"] = item["Buy_price"]

              #Check if movie already existed.
              movie_title = item['Movie_title']
              cur.execute("""SELECT auto_id FROM tbl_movies WHERE title LIKE %s""", [movie_title])
              movie_set = cur.fetchall()
              
              if(movie_set):
                for row in movie_set:
                    movie_id = row[0]
                    sql = "SELECT auto_id FROM tbl_prices WHERE movie_id = %s AND vendor_id = %s" % (movie_id,Vendor_id)
                    cur.execute(sql)
                    price_set = cur.fetchall()
                    if(price_set):
                      cur.execute ("UPDATE tbl_prices SET video_url=%s, unique_id=%s, Rent_sd_price=%s, Rent_hd_price=%s, Buy_sd_price=%s, Buy_hd_price=%s, updated_date=%s  WHERE movie_id=%s AND vendor_id=%s", (item["Video_urls"],item["Unique_id"],item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"], created_date,movie_id,Vendor_id))
                      #print cur._last_executed
                    else:
                      insert_sql = "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                      cur.execute(insert_sql,(movie_id,item["Video_urls"],item["Unique_id"],Vendor_id,item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"], created_date,created_date))
              else:
                ##Inserting into movies table
                insert_sql1 = "INSERT INTO tbl_movies (title,thumbnail_url,release_year) VALUES(%s,%s,%s)"
                cur.execute(insert_sql1,(item["Movie_title"],item["Thumb_urls"],item["Release_year"]))
                movie_id    = cur.lastrowid
                ##Inserting into prices table (need to update but_price,buyhd_price)
                insert_sql2 =  "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(insert_sql2,(movie_id,item["Video_urls"],item["Unique_id"],Vendor_id,item["Rent_sd_price"],item["Rent_hd_price"],item["Buy_sd_price"],item["Buy_hd_price"],created_date,created_date))
        
                self.conn.commit()
              return item
            ########END:: Itunes movies #########################################################
            if(item and spider.name == 'beinconnect'):
              Vendor_id = 4 
              #Check if movie already existed.
              #cur.execute("SELECT auto_id  FROM tbl_movies WHERE title = '"+item['Movie_title']+"'")
              #cur.execute('SELECT auto_id  FROM tbl_movies WHERE title = "'+item['Movie_title']+'"')
              #movie_set = cur.fetchall()
              movie_title = item['Movie_title']
              cur.execute("""SELECT auto_id FROM tbl_movies WHERE title LIKE %s""", [movie_title])
              movie_set = cur.fetchall()
              if(movie_set):
                for row in movie_set:
                    movie_id = row[0]
                    sql = "SELECT auto_id FROM tbl_prices WHERE movie_id = %s AND vendor_id = %s"% (movie_id,Vendor_id) 
                    cur.execute(sql)
                    price_set = cur.fetchall()
                    if(price_set):
                      update_sql = "UPDATE tbl_prices SET video_url=%s, unique_id=%s, Rent_sd_price=%s, Rent_hd_price=%s, Buy_sd_price=%s, Buy_hd_price=%s, updated_date=%s  WHERE movie_id=%s AND vendor_id=%s"
                      cur.execute (update_sql,(item["Thumb_urls"],'0',0,0,0,0,created_date,movie_id,Vendor_id))
                      #print cur._last_executed
                    else:
                      insert_sql = "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,is_subscribe,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                      cur.execute(insert_sql,(movie_id,item["Thumb_urls"],'0',Vendor_id,0,0,0,0,'1',created_date,created_date))
              else:
                  ##Inserting into movies table
                if(item["Movie_title"]): 
                    insert_sql1 =  "INSERT INTO tbl_movies (title,thumbnail_url,release_year) VALUES(%s,%s,%s)"
                    cur.execute(insert_sql1,(item["Movie_title"],item["Thumb_urls"],item["Release_year"]))
                    movie_id    = cur.lastrowid
                    ##Inserting into prices table (need to update but_price,buyhd_price)
                    insert_sql2 =  "INSERT INTO tbl_prices (movie_id,video_url,unique_id,vendor_id,Rent_sd_price,Rent_hd_price,Buy_sd_price,Buy_hd_price,is_subscribe,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cur.execute(insert_sql2,(movie_id,item["Video_urls"],'0',Vendor_id,0,0,0,0,'1',created_date,created_date))
                          
                    self.conn.commit()
              return item
            ########START:: Beinconnect movies #######################################################

            ########START:: Beinconnect movies #######################################################

        
