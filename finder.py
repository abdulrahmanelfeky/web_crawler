import  HTMLParser
from  urllib import  parse


class Finder(HTMLParser.HTMLParser):

    prevent_char = ['\n','  ']
    def __init__(self):
        self.data=set()
        self.links=set()
        self.baseurl  = ""
        self.reset()
    def handle_data(self, data):
        if not data in self.prevent_char:
            self.data.add(data)
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (att,val) in attrs:
                if att == 'href':
                   self.links.add( parse.urljoin(self.baseurl,val))

    def return_data(self):
        return  self.data
    def return_links(self):
        return  self.links
