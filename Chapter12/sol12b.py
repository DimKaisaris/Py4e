#extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name
#in the list, follow that link and repeat the process a number
# of times and report the last name you find.)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
position = input('Enter position: ')

# Retrieve all of the anchor tags
print("Retrieving",url)
tags = soup('a')
for i in range(int(count)):
    links = []
    for tag in tags:
        links.append(str(tag.get('href', None)))

    html = urllib.request.urlopen(links[int(position)-1], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving",links[int(position)-1])
    tags = soup('a')
