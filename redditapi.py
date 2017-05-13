import urllib.request
from html.parser import HTMLParser


from html.parser import HTMLParser

class ParseContent(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = ParseContent()





usr = ""
postnum = 0
url = "https://www.reddit.com/user/"+usr+"/"+str(postnum)
hdr = { 'User-Agent' : 'metaprinter' }
req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()

html = html.decode("utf-8")


parser.feed(html)