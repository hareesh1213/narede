# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from crawlers.items import CrawlersItem
import urlparse
import re
import time,datetime


class BeinconnectSpider(CrawlSpider):
    name = 'beinconnect'
    allowed_domains = ['beinconnect.com.tr']
    start_urls = ['https://www.beinconnect.com.tr']

    ##Crawler rules for extracting data from allowed URLs only.
    rules = (
              Rule(LinkExtractor(allow=('/film/?')),callback="parse_item",follow=True),
		      Rule(LinkExtractor(allow=('/ulusal/?')),callback="parse_item",follow=True),
		      Rule(LinkExtractor(allow=('/dizi/?')),callback="parse_item",follow=True),
              Rule(LinkExtractor(allow=('/yabanci-dizi/?')),callback="parse_item",follow=True) 
            )

    ##Function parse item which will get response from crawler class and process it for data extraction.  
    def parse_item(self,response):
        hxs = scrapy.Selector(response)
        webdata = hxs.xpath('/html')
        items = []

        ##For loop for repeatedly getting data from urls via xpath.      
        for getdata in webdata  :
            item = CrawlersItem()

            item["Movie_title"]   = ''.join(response.css("div.content-headings h1::text").extract()).encode('utf-8')
            item["Thumb_urls"] 	  = response.css("img.season-design::attr('src')").extract()
            item["Video_urls"]    = response.url
            item["Release_year"]  = response.css("span#content-detail-production-year::text").extract()
            
            if(item["Release_year"]!=""):
                item["Release_year"] =  time.strftime("%Y-%m-%d")
            '''rawyear  =  response.xpath('//*[@class="content-info"]/p[normalize-space()]/text()').extract()
            if(rawyear):
                relyear  =  rawyear[9].replace(u' ',u'')
                onlyyear =  relyear.replace(u'\n',u'')
                item["Release_year"] =  onlyyear+'-01-01'
            else:
                item["Release_year"] =  time.strftime("%Y-%m-%d")'''
            items.append(item)
        return items

