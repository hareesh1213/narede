# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItunescrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Thumb_urls = scrapy.Field()
    Video_urls = scrapy.Field()
    Movie_title = scrapy.Field()
    Movie_price = scrapy.Field()
    Release_year = scrapy.Field()

    Rent_price      = scrapy.Field()
    Buy_price       = scrapy.Field()
    Buyhd_price     = scrapy.Field()
    Rent_sd_price   = scrapy.Field()
    Rent_hd_price   = scrapy.Field()
    Buy_sd_price    = scrapy.Field()
    Buy_hd_price    = scrapy.Field()
    PriceObj        = scrapy.Field()

    Unique_id = scrapy.Field()
    Link = scrapy.Field()
    Item_name = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Filesize = scrapy.Field()
    Downloads = scrapy.Field()
    Version = scrapy.Field()
    Compatibility = scrapy.Field()
    Content_rating = scrapy.Field()
    Author_link = scrapy.Field()
##  Author_link_test = scrapy.Field()
    Genre = scrapy.Field()
    Price = scrapy.Field()
    Rating_value = scrapy.Field()
    Review_number = scrapy.Field()
    Description = scrapy.Field()
    IAP = scrapy.Field()
    Developer_badge = scrapy.Field()
    Physical_address = scrapy.Field()
    Video_URL = scrapy.Field()
    Developer_ID = scrapy.Field()
