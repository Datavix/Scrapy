#############################################################
### Date:    2016.02.15
### Author:  Linfeng Cai
### Purpose: Retrieve all the community urls under Beijing ershoufang
#############################################################

import scrapy
import os.path
from scrapy.http import Request
from sets import Set

class CommunitySpider(scrapy.Spider):
    name = "community"
    allowed_domains = ["bj.sofang.com"]
    base_url = "http://bj.sofang.com/"

    # Initial url for crawling
    start_urls = [ "http://bj.sofang.com/zufang.htm?housetype=%E4%BD%8F%E5%AE%85"]

    # Output folder 
    output_folder = "/home/zc/Software/scrapy/tutorial/tutorial/link/"
    filename = output_folder + "community.html"

    # Distinct communities stores in a set
    community_pool = Set() 
    
    # Callback funtion, retrieve http response
    def parse(self, response):
        # Current community link
        current_link = '//tr/td/div/p/a/@href'
        for sel in response.xpath(current_link):
            link = sel.extract()
            link = self.base_url[:-1] + link
     	    with open(self.filename, 'a') as f:
            	f.write(link + "\n")
            # print link
        
        # Links for next iteration
        next_links = '//div[@class="list_msg"]/div/ul/li/a/@href'	
        for sub in response.xpath(next_links):
	        link = sub.extract()
	        page_number = link.split("=")[-1]

            # If page number not in community pool, send new request to the page and register th parse callback
	        if page_number not in self.community_pool:
	            self.community_pool.add(page_number)
	            link = self.base_url + link
	            yield Request(url=link, callback=self.parse) 

