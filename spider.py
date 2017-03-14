from urllib.request import urlopen, Request
import urllib.response
from  urllib import parse
import HTMLParser
import html
from finder import Finder

from  store import *


class spider:
    website_name = ''
    website_url = ''
    links_website = []
    links_crawled = []
    data_dict = {}

    def __init__(self, website_name, website_url):
        spider.website_name = website_name
        spider.website_url = website_url
        self.initialize()

    def initialize(self):
        create_Folder_website(spider.website_name)
        create_data_files(spider.website_name, spider.website_url)
        spider.links_website = file_to_set(spider.website_name + "/linksofwebsite.txt")
        spider.links_crawled = file_to_set(spider.website_name + "/linkscrawled.txt")

    @staticmethod
    def crawl(url):
        if not url in spider.links_crawled:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req) as urldata:
                data = urldata.read()
            f = Finder()
            f.baseurl=spider.website_url
            data = data.decode('utf-8')
            data = html.unescape(data)
            f.feed(data)
            f.close()
            links=f.return_links()
            spider.links_website.remove(url)
            for val in links:
               spider.links_website.append(val)

            spider.links_crawled.append(url)
            spider.data_dict[url] = f.return_data()

    @staticmethod
    def search_in_website(keyword):
        for key in spider.links_crawled:
            if keyword in spider.data_dict[key]:
                return key
        return ""

    @staticmethod
    def update_files():
        set_to_file(spider.website_name + "/linksofwebsite.txt", spider.links_website)
        set_to_file(spider.website_name + "/linkscrawled.txt", spider.links_crawled)
