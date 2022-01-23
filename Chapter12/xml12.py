import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
hand = urllib.request.urlopen(url)
data = hand.read()
print('Retrieved', len(data), 'characters')

sum=0
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print("Count:",len(counts))
for count in counts:
    v = count.text
    z = int(v)
    sum = sum + z
print(sum)
