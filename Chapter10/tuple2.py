d={'a':10,'b':1,'c':22}
print(d.items())
print(sorted(d.items()))
x=(12,7,4,10,2,5,1,13,16,8,14)
print(sorted(x,reverse=True))
for (k,v) in sorted(d.items()):
    print (k,v)

tmp=list()
for (k,v) in d.items():
    tmp.append((v,k))   #list of tuples
print(tmp)
print(sorted(tmp,reverse=True))
