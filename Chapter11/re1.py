import re

hand=open('mbox-short.txt')
for line in hand:
    line.rstrip()
    if re.search('^From: ', line):
        print(line)
