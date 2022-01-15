import re
count=0
hand=open('ex11.txt')
for line in hand:
    line.rstrip()
    n=re.findall('[0-9]+',line)
    for x in n:
          z=int(x)
          count=count + z
print(count)
