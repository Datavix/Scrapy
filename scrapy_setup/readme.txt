Install scrapy: http://doc.scrapy.org/en/latest/intro/install.html

ubuntu:
1. Create a folder which you want to put the scrapy project in
2. Copy 'ershoufang' project into this folder
3. Modify 'ershoufang.spider.py' under 'ershoufang/ershoufang/spiders', change 'output_folder', 'input_filename', 'output_filename', and 'json_file' as follows
output_folder: root folder path
input_filename: the path where you put home.html (go to 'Scrapy/soufang/result' on github, download 'home.html.tar.gz' and extract to get home.html)
output_filename: A folder will store all the crawled html pages (make sure the disk contains this folder has 150G free space)
json_file: json file stores all the result keyword mapping
5. Go to 'ershoufang/ershoufang/' directory and run 'scrapy crawl ershoufang' to start crawling


