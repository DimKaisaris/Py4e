import urllib.request
import xml.etree.ElementTree as ET

result = 0

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print("Count:",len(counts))
for count in counts:
    value = count.text
    result = result + int(value)
print("Sum: ",result)
