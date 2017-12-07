#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        categoryUrl = request.url
        if '/tr/movie/' in request.url:
            ua = 'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-us'
        else:
            ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
        if ua:
            request.headers.setdefault('User-Agent', ua)
