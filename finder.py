import  HTMLParser



class Finder(HTMLParser.HTMLParser):
    def __init__(self):
        self.data=set()
        self.links=set()
    def handle_data(self, data):
        pass
    def handle_starttag(self, tag, attrs):
        pass
    def return_data(self):
        return  self.data
    def return_links(self):
        return  self.links
