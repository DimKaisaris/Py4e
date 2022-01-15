from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter - ')
html=urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retriece all of the anchor tags
tags= soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href',None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
