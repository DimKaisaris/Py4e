fh=open('test.txt')
for line in fh:
    line.strip()
    z=line.split()
    if z[0]=='When':
        print('hi')
