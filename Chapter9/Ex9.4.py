fh = open("mbox-short.txt")
counts=dict()
for line in fh:
    line.rstrip()
    z=line.split()
    if z==[]:     # so to skip the blank lines
        continue
    else :
        if z[0]=='From':
            counts[z[1]]=counts.get(z[1],0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
