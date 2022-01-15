fh = open("mbox-short.txt")
counts=dict()
lst=list()
for line in fh:
    line.rstrip()
    z=line.split()
    if z==[]:     # so to skip the blank lines
        continue
    else :
        if z[0]=='From':
            x=z[5].split(':')
            counts[x[0]]=counts.get(x[0],0)+1
for (k,v) in counts.items():
    newtup=k,v
    lst.append(newtup)
lst=sorted(lst)
for k,v in lst:
    print(k,v)
