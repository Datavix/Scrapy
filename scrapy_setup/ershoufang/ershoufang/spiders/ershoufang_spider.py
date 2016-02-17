#############################################################
### Date:    2016.02.15
### Author:  Linfeng Cai
### Purpose: Retrieve keywords: update time, price, average price, house design, size, orientation, floor
###          property management, year, location, facilities, traffic and phone from each home
#############################################################

import scrapy
import os.path
from scrapy.http import Request
from ershoufang.items import ErshoufangItem
import json

class ErshoufangSpider(scrapy.Spider):
    name = "ershoufang"
    allowed_domains = ["bj.sofang.com"]
    base_url = "http://bj.sofang.com/"

    # Output folder
    output_folder = "/home/zc/Software/scrapy/"
    input_filename = output_folder + "soufang/soufang/link/home.html"
    output_filename = "/media/zc/Entertainment/ershoufang/"

    # Json file stores all the keywords mapping
    json_file = output_folder + "ershoufang/ershoufang/result/result.jl"
    openFile = open(json_file, 'a')
	
    # Keyword XPath
    update_time = '//div[@class="product_name"]/p/text()'
    price = '//div[@class="detail_msg"]/ul/li/span[@class="price"]/text()'
    average_price = '//div[@class="detail_msg"]/ul/li/font/text()'
    houseDesign_size_orientation_floor = '//div[@class="detail_msg"]/ul/li[@class="margin1"]/span[@class="width2"]/span[@class="black"]/text()'
    propertyManagement_year = '//div[@class="detail_msg"]/ul/li[@class="margin"]/span[@class="width2"]/span[@class="black"]/text()'
    location_facilities = '//div[@class="detail_msg"]/ul/li[@class="width3 margin1"]/span[@class="content"]/text()'
    traffic = '//div[@class="detail_msg"]/ul/li[@class="width3 margin"]/span[@class="content"]/text()'
    phone = '//div[@class="detail_msg"]/ul/li/span[@class="phone width"]/text()'
    
    # Read all home in home.html, store as list in start_urls
    with open(input_filename) as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        # Write each home url responses into a html file f0r backup purpose
        filename = os.path.join(self.output_filename, response.url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.body)

        # Retrieve each keyword information into item object
        item = ErshoufangItem()
        item['update_time'] = response.xpath(self.update_time).extract()
        item['price'] = response.xpath(self.price).extract()
        item['average_price'] = response.xpath(self.average_price).extract()
        item['houseDesign_size_orientation_floor'] = response.xpath(self.houseDesign_size_orientation_floor).extract()
        item['propertyManagement_year'] = response.xpath(self.propertyManagement_year).extract()
        item['location_facilities'] = response.xpath(self.location_facilities).extract()
        item['traffic'] = response.xpath(self.traffic).extract()
        item['phone'] = response.xpath(self.phone).extract()

        # Dump the data into json format
        line = json.dumps(dict(item)) + "\n"
        self.openFile.write(line)
	
