#importing system libraries
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from crawlers.items import CrawlersItem
import urlparse
import re
import time,datetime

##Master Class which runs crawler with its name.
class ItunesSpider(CrawlSpider):
    name = 'itunes'
    allowed_domains = ['itunes.apple.com']
    #start_urls = ['https://itunes.apple.com/us/genre/movies/id33']
    start_urls = ['https://itunes.apple.com/tr/genre/films/id33']

	##Crawler rules for extracting data from allowed URLs only.
    rules = (
		        Rule(LinkExtractor(allow=('/tr/genre/films-(.*?)/(.*?)')),callback="parse_item",follow=True),
		        Rule(LinkExtractor(allow=('/tr/movie/(.*?)/(.*?)')),callback="parse_item",follow=True)
	        )

	##Function parse which will get response from crawler class and process it for data extraction. 
    def parse_item(self, response):
        hxs 	= 	scrapy.Selector(response)
        webdata = hxs.xpath('/html')
     	items = []

		##For loop for repeatedly getting data from urls via xpath.      
      	for getdata in webdata:
            item = CrawlersItem()
            item["Rent_price"] = 0
            item["Buy_price"] = 0
            item["Rent_sd_price"] = 0
            item["Rent_hd_price"] = 0
            item["Buy_sd_price"] = 0
            item["Buy_hd_price"] = 0

            videoUrl			=	response.css("img.artwork::attr('src-swap-high-dpi')").extract_first()

            if videoUrl:
              item["Thumb_urls"] 		= response.css("img.artwork::attr('src-swap-high-dpi')").extract_first()#''.join(webdata.xpath('//*[@class="top-level-genre"]/text()').extract())
              #item["Buy_price"]  	= response.css("span.price > span::text").extract_first().replace("$", "") #''.join(getdata.xpath('//*[@src-swap-high-dpi]/text()').extract())
              releaseDateObj  = response.css("li.release-date")
              Raw_string      = ''.join(releaseDateObj.css("span::attr('content')").extract())

              Release_string      = re.split('(\d+)',Raw_string)
              Release_string_month= Release_string[2]
              Release_month       = month_converter(Release_string_month.lower().replace(" ",""))
              Release_year        = Release_string[3].replace(" ","")
              Release_date        = 1
              #item["Release_year"]= Release_date+Release_month+Release_year
              #print Release_date
              #print Release_month
              #print Release_year
              Final_date_str      = str(Release_year)+str('-')+str(Release_month)+str('-')+str(Release_date)
              item["Release_year"]=datetime.datetime.strptime(Final_date_str, '%Y-%m-%d').date()

              priceObj = response.css("span.price::text").extract()
              priceLblObj = response.css("span.action::text").extract()

              if 1 < len(priceObj):
                item["Buy_hd_price"]  = priceObj[0].replace(u'TL', u'').replace(',', '.').rstrip()
              if 2 < len(priceObj):
                item["Rent_hd_price"] = priceObj[1].replace(u'TL', u'').replace(',', '.').rstrip()
              if 3 < len(priceObj):
                item["Buy_sd_price"]  = priceObj[2].replace(u'TL', u'').replace(',', '.').rstrip()
              if 4 < len(priceObj):
                item["Rent_sd_price"] = priceObj[3].replace(u'TL', u'').replace(',', '.').rstrip()

              item["Video_urls"]  = response.url
              item["Movie_title"] = response.css("button.view-trailer::attr('preview-title')").extract_first()
              item["Unique_id"]  	= item["Video_urls"].split('/')[-1]
              items.append(item)
              if items:
                return items
                
              else:
                return True

def month_converter(month):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    return months.index(month) + 1