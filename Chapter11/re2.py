import re
x='From: Using the: character'
y=re.findall('^F.+:',x)  #Greedy
print(y)

z=re.findall('F.+?:',x) #Not Greedy(?)
print(z)

d='from stephen.marquard@uct.za Sat Jan 5 09:14:16 2008'
w=re.findall('\S+?@\S+',d)   #\S+ at least one non Whitespace
print('This one:')
print(w)

c=re.findall('^from (\S+@\S+)', d) #it gets only whats inside()
print(c)
