import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1598722.json"

data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)

numbers = []
for item in info['comments']:
  ints = int(item['count'])
  numbers.append(ints)
  
sum(numbers)
