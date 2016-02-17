from lxml import html
from os import listdir
import os.path
import json

output_folder = "/home/zc/Software/scrapy/"
json_file = output_folder + "ershoufang/ershoufang/result/result_correct.jl"
souce_file_path = '/media/zc/Entertainment/ershoufang/'

onlyfiles = [f for f in listdir(souce_file_path)]

openFile = open(json_file, 'a')

for filename in onlyfiles:
    if filename.endswith(".htm"):
        with open(os.path.join(souce_file_path, filename), 'r') as myfile:
            dictionary = {}
            data = myfile.read()
            tree = html.fromstring(data)
	
	    update_time = tree.xpath('//div[@class="product_name"]/p/text()')
	    price = tree.xpath('//div[@class="detail_msg"]/ul/li/span[@class="price"]/text()')
	    average_price = tree.xpath('//div[@class="detail_msg"]/ul/li/font/text()')
	    houseDesign_size_orientation_floor = tree.xpath('//div[@class="detail_msg"]/ul/li[@class="margin1"]/span[@class="width2"]/text()')
	    propertyManagement_year = tree.xpath('//div[@class="detail_msg"]/ul/li[@class="margin"]/span[@class="width2"]/text()')
	    location_facilities = tree.xpath('//div[@class="detail_msg"]/ul/li[@class="width3 margin1"]/span[@class="content"]/text()')
	    traffic = tree.xpath('//div[@class="detail_msg"]/ul/li[@class="width3 margin"]/span[@class="content"]/text()')
	    phone = tree.xpath('//div[@class="detail_msg"]/ul/li/span[@class="phone width"]/text()')

	    dictionary['update_time'] = update_time
	    dictionary['price'] = price
	    dictionary['average_price'] = average_price
	    dictionary['houseDesign_size_orientation_floor'] = houseDesign_size_orientation_floor
	    dictionary['propertyManagement_year'] = propertyManagement_year
            dictionary['location_facilities'] = location_facilities
	    dictionary['traffic'] = traffic
	    dictionary['phone'] = phone

	    line = json.dumps(dictionary) + "\n"
	    openFile.write(line)
