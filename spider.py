from urllib.request import urlopen, Request
import urllib.response
from  urllib import parse
import HTMLParser
from finder import Finder

from  store import *
class spider:
    website_name =''
    website_url=''
    links_website=set()
    links_crawled=set()
    def __init__(self,website_name,website_url):
        spider.website_name=website_name
        spider.website_url-website_url
        spider.initialize()
    @staticmethod
    def initialize(self):
        create_Folder_website(self.website_name)
        create_data_files(spider.website_name,spider.website_url)
        spider.links_website=file_to_set(spider.website_name+"/linksofwebsite.txt")
        spider.links_crawled=file_to_set(spider.website_name+"/linkscrawled.txt")
    @staticmethod
    def crawl(self, url):
        if not url in  spider.links_crawled:
            pass



