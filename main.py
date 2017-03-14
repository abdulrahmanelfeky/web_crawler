from spider import *
import  threading
print ("WebSite Name:\n ")
website_name=input()
print("WebSite URL:\n")
website_url=input()
spider(website_name,website_url)

sete=set()
sete.add('http://maps.google.com.eg/maps?hl=ar&tab=wl')

for url in spider.links_website:
    try:
     spider.crawl(url)
     spider.update_files()
     print( "found in " + spider.search_in_website("gta"))
    except:
        print(url)
spider.update_files()
