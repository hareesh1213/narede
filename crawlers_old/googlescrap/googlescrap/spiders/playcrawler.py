#importing system libraries
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from googlescrap.items import GooglescrapItem
import urlparse
import re
import time,datetime

##Master Class which runs crawler with its name.
class MySpider(CrawlSpider):
  name = "playcrawler"
  allowed_domains = ["play.google.com"]
  start_urls = ["https://play.google.com/store/movies"]

  ##Crawler rules for extracting data from allowed URLs only.
  rules = (
            Rule(LinkExtractor(allow=('/store/movies')),callback="parse_item",follow=True),
            Rule(LinkExtractor(allow=('/store/movies/details\?')),callback="parse_item",follow=True)
          )

  ##Function parse item which will get response from crawler class and process it for data extraction.  
  def parse_item(self,response):
      hxs = scrapy.Selector(response)
      webdata = hxs.xpath('/html')
      items = []

      ##For loop for repeatedly getting data from urls via xpath.      
      for getdata in webdata  :
          item = GooglescrapItem()

          item["Rent_price"]    = 0
          item["Buy_price"]     = 0
          item["Rent_sd_price"] = 0
          item["Rent_hd_price"] = 0
          item["Buy_sd_price"]  = 0
          item["Buy_hd_price"]  = 0

          item["Movie_title"] = ''.join(getdata.xpath('//*[@class="AHFaub"]/text()').extract())
          if item["Movie_title"]:
              item["Thumb_urls"]  = ''.join(getdata.xpath('//*[@class="T75of yNMUz Nywl9c"]/@src').extract())
              item["Video_urls"]  = ''.join(getdata.xpath('head/link[4]/@href').extract())
              item["Unique_id"]   = item["Video_urls"].split('?id=')[-1]
              price_string        = ''.join(getdata.xpath('//*[@class=" ScJHi LkLjZd HPiPcc IfEcue   "]/text()').extract())
              #price_string        = price_string.replace(u'\u20b9\xa0', u' ')
              price_string        = price_string.replace(u'\u0024',u' ')
              #price_string        = price_string.replace(u'\$', u'')
              #item["Release_year"]= ''.join(getdata.xpath('//*[@class="UAO9ie"]/text()').extract())

              Raw_string          = ''.join(getdata.xpath('//*[@class="UAO9ie"]/text()').extract())
              Release_string      = re.split('(\d+)',Raw_string)
              Release_string_month= Release_string[0]
              Release_month       = month_converter(Release_string_month.lower().replace(" ",""))
              Release_year        = Release_string[1].replace(" ","")
              Release_date        = 1
              #print Release_date
              #print Release_month
              #print Release_year
              Final_date_str      = str(Release_year)+str('-')+str(Release_month)+str('-')+str(Release_date)
              item["Release_year"]=datetime.datetime.strptime(Final_date_str, '%Y-%m-%d').date()


              price_string        = price_string.strip()
              price_list          = price_string.split()
              price_list_size     = len(price_string.split())

              ##Getting data if we have only bye or rent prices. 
              if(price_list_size == 2 and price_list[1]=="Rent"):
                item["Rent_price"] = price_list[0]
              elif(price_list_size == 2 and price_list[1]=="Buy"):
                item["Buy_price"] = price_list[0]

              ##Getting data if we have only bye and rent sd or hd prices.
              elif(price_list_size == 3 and price_list[1]=="Rent" and price_list[1]=="SD"):
                item["Rent_sd_price"] = price_list[0]
              elif(price_list_size == 3 and price_list[1]=="Rent" and price_list[1]=="HD"):
                item["Rent_hd_price"] = price_list[0]
              elif(price_list_size == 3 and price_list[1]=="Buy" and price_list[1]=="SD"):
                item["Buy_sd_price"] = price_list[0]
              elif(price_list_size == 3 and price_list[1]=="Buy" and price_list[1]=="HD"):  
                item["Buy_hd_price"] = price_list[0]

              ##Getting data if we have only bye or rent sd and hd prices.
              elif(price_list_size == 5 and price_list[1]=="Rent" and price_list[3]=="Buy" and price_list[4]=="SD"):
                item["Rent_price"]   = price_list[0]
                item["Buy_sd_price"] = price_list[2]

              elif(price_list_size == 5 and price_list[1]=="Rent" and price_list[3]=="Buy" and price_list[4]=="HD"):
                item["Rent_price"]   = price_list[0]
                item["Buy_hd_price"] = price_list[2]

              elif(price_list_size == 5 and price_list[1]=="Rent" and price_list[2]=="SD" and price_list[4]=="Buy"):
                item["Buy_price"]   = price_list[3]
                item["Rent_sd_price"] = price_list[0]

              elif(price_list_size == 5 and price_list[1]=="Rent" and price_list[2]=="HD" and price_list[4]=="Buy"):
                item["Buy_price"]   = price_list[3]
                item["Rent_hd_price"] = price_list[0]

              ##Getting data if we have simply bye and rent prices.
              elif(price_list_size == 4):
                item["Rent_price"] = price_list[0]
                item["Buy_price"] = price_list[2]

              ##Getting data if we have rent and bye with sd and hd both prices.
              elif(price_list_size == 6 and price_list[1]=="Rent" and price_list[2]=="SD" and price_list[4]=="Buy" and price_list[5]=="SD"):
                item["Rent_sd_price"] = price_list[0]
                item["Buy_sd_price"] = price_list[3]
              elif(price_list_size == 6 and price_list[1]=="Rent" and price_list[2]=="HD" and price_list[4]=="Buy" and price_list[5]=="SD"):
                item["Rent_hd_price"] = price_list[0]
                item["Buy_sd_price"] = price_list[3]
              elif(price_list_size == 6 and price_list[1]=="Rent" and price_list[2]=="SD" and price_list[4]=="Buy" and price_list[5]=="HD"):
                item["Rent_sd_price"] = price_list[0]
                item["Buy_hd_price"] = price_list[3]
              elif(price_list_size == 6 and price_list[1]=="Rent" and price_list[2]=="HD" and price_list[4]=="Buy" and price_list[5]=="HD"):
                item["Rent_hd_price"] = price_list[0]
                item["Buy_hd_price"] = price_list[3]


                item["Genre"]          = ''.join(getdata.xpath('//*[@itemprop="genre"]/text()').extract())
                item["Content_rating"] = ''.join(getdata.xpath('//*[@itemprop="contentRating"]/text()').extract())

              items.append(item)
      return items
def month_converter(month):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    return months.index(month) + 1

