text = 'With three words'
stuff = text.split() # sererates using the spaces, makes list
print(stuff)
print(len(stuff))
print(stuff[0])
for i in stuff:
    print(i)
text2 = 'A  lot     of   spaces'
stuff2 =text2.split()
print(stuff2)
line = 'first,second,third'
stuff3 = line.split()
print(stuff3)
print(len(stuff3))
stuff3 = line.split(',') # specify delimiter
print(stuff3)
print(len(stuff3))
