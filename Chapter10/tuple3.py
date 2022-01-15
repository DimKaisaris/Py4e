name=input('Enter File: ')
handle=open(name)
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)
lst=sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)

print(sorted([(val,key) for key,val in counts.items()],reverse=True))
print('Try :')
z=(sorted([(val,key) for key,val in counts.items()],reverse=True))
for val,key in z[:10]:
    print(key,val)
