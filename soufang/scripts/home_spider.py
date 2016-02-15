#############################################################
### Date:    2016.02.15
### Author:  Linfeng Cai
### Purpose: Retrieve all the home urls in all communities under Beijing ershoufang
#############################################################

import scrapy
import os.path
from scrapy.http import Request
from sets import Set

class HomeSpider(scrapy.Spider):
    name = "home"
    allowed_domains = ["bj.sofang.com"]
    base_url = "http://bj.sofang.com/"

    # Output folder 
    output_folder = "/home/zc/Software/scrapy/"

    input_filename = output_folder + "tutorial/tutorial/link/community.html"
    output_filename = output_folder + "soufang/soufang/link/home.html"

    # Distinct home stores in a set
    home_pool = Set()

    # Read all communities in community.html, store as list in start_urls
    with open(input_filename) as f:
        start_urls = [url.strip() for url in f.readlines()]

    # Callback funtion, retrieve http response
    def parse(self, response):
        # Current home link
        current_link = '//tr/td/div[@class="house_msg"]/p/a/@href'
        for sel in response.xpath(current_link):
            link = sel.extract()
            link = self.base_url[:-1] + link
     	    with open(self.output_filename, 'a') as f:
            	f.write(link + "\n")		 		
            # print link

        # Links for next iteration
        next_links = '//div[@class="page"]/ul/li/a/@href'
        for sub in response.xpath(next_links):
	        link = sub.extract()

            # If page number not in community pool, send new request to the page and register th parse callback
	        if link not in self.home_pool:
	            self.home_pool.add(link)
	            link = self.base_url[:-1] + link
	            yield Request(url=link, callback=self.parse) 
