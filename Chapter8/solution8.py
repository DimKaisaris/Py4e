han = open('mbox-short.txt')
count=0
for line in han:
    line=line.rstrip()
    wds=line.split()
    if len(wds)<1:     # skip the blank lines(Guardian pattern)
        continue       #other way : if line =='' : continue
    if wds[0] != 'From' :
        continue
    print(wds[1])
    count=count+1
print(count)

# guardian in a compound statement:
#if len(wds)<1 or wds[0] != 'from' : continue
