import re
hand=open('mbox-short.txt')
numlist=list()
for line in hand:
    line.strip()
    stuff=re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num=float(stuff[0])
    numlist.append(num)
print(numlist)
print('Max= ',max(numlist))

y='We just received $10.00 for cookies!'
x=re.findall('\$[0-9.]+',y)
print(x)
