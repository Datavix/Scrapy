
import scrapy
from scrapy.http import Request
from mp.items import MpItem
import json
import string
import datetime
import re

from sets import Set

class MpSpider(scrapy.Spider):
    name = "mp"
    allowed_domains = ["www.meipai.com"]
    start_urls = ["http://www.meipai.com/media/571939984"]
    base_url = "http://www.meipai.com"

    # Output folder 
    output_folder = "/home/datavix/project/mp/result/"

    # Json file stores all the keywords mapping
    json_file = output_folder + datetime.datetime.now().strftime ("%Y%m%d") + "_mp_result.jl"
    openFile = open(json_file, 'w')
    link_pool = set()

    def replaceStr(self, inputStr):
        inputStr = re.sub(r'\n', ' ', str(inputStr))
        inputStr = inputStr.replace("\\n", "")
        inputStr = inputStr.replace("  ", "")
        inputStr = inputStr.replace("[u'", "")
        inputStr = inputStr.replace("']", "")
        return inputStr

    # Callback funtion, retrieve http response
    def parse(self, response):
        item = MpItem()
	main_page_links = response.xpath('//div[@class="nav max center pr"]/a/@href').extract()
	if len(main_page_links) > 0:
	    for main_page_link in main_page_links:
		main_page_link = self.base_url + main_page_link
		if main_page_link not in self.link_pool:
                    self.link_pool.add(main_page_link)
		    yield Request(url=main_page_link, callback=self.parse)

	video_links = response.xpath('//li[@class="pr no-select loading  J_media_list_item"]/div/a/@href').extract()	
	if len(video_links) > 0:
            for video_link in video_links:
		if not video_link.startswith('http'):
                   video_link = self.base_url + video_link
		if video_link not in self.link_pool:
		    self.link_pool.add(video_link)
               	    yield Request(url=video_link, callback=self.parse)
    
	title = response.xpath('//h1[@class="detail-description break js-convert-emoji"]/text()').extract()
	if len(title) > 0:
		item['title'] = title
		item['url'] = response.url
		ext_links = response.xpath('//li[@class="detail-li pr"]/a/@href').extract()
		for ext_link in ext_links:
		    ext_link = self.base_url + ext_link
		    if ext_link not in self.link_pool:
			self.link_pool.add(ext_link)
			yield Request(url=ext_link, callback=self.parse)
		int_links = response.xpath('//ul[@class="detail-ul clearfix pr"]/li[@class="pr fl cp"]/a/@href').extract()
		for int_link in int_links:
		    int_link = self.base_url + int_link
                    if int_link not in self.link_pool:
                        self.link_pool.add(int_link)
                        yield Request(url=int_link, callback=self.parse)

		# Dump the data into json format
		line = json.dumps(dict(item)) + "\n"
		self.openFile.write(line)
