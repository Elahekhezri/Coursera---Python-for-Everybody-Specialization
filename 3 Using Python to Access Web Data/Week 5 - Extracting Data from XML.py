import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1598721.xml"

xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)

counts = tree.findall('comments/comment/count')

numbers = []
for item in counts:
  ints = int(item.text)
  numbers.append(ints)

sum(numbers)
  
