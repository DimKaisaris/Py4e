# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
p=0
for line in fh :
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    x=line.find(':')
    y=line[x+1:]
    z=float(y)
    p=p+z
d=p/count
print('Average spam confidence:', d )
