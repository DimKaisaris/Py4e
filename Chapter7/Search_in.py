fname=input('Enter the file name : ')
try:
    text = open(fname)
except:
    print('file cannot be found',fname)
    quit()
for line in text :
    line=line.strip()
    if not 'to' in line:
        continue
    print(line)
