import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
hand = urllib.request.urlopen(url)
info = hand.read()
data = json.loads(info)
print('Retrieved', len(str(data)), 'characters')
