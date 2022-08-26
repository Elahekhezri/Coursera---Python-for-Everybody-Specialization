import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

address = "University of Kerala"

parameters = {"address": address, "key":api_key}    

url = serviceurl + urllib.parse.urlencode(parameters)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
    
js = json.loads(data)

    
print(json.dumps(js, indent=4))

place_id = js["results"][0]["place_id"]
