# Assignment

## In this assignment you will write a Python program to use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file

# Answer
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen("http://py4e-data.dr-chuck.net/comments_1598719.html", context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

numbs = [tag.string for tag in tags]

ints = [int(x) for x in numbs]

print(sum(ints))
