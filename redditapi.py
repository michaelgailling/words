import urllib.request
from Parser import ParseContent

#Crreate new handler for the parser class
parser = ParseContent()

usr = ""
postnum = 0
url = "https://www.reddit.com/user/"+usr+"/"+str(postnum)
hdr = { 'User-Agent' : 'metaprinter' }
req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()

html = html.decode("utf-8")


parser.feed(html)