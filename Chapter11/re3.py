import re
d='from stephen.marquard@uct.za Sat Jan 5 09:14:16 2008'
y=re.findall('@([^ ]*)',d)
print(y)
x=re.findall('^from .+@([^ ]*)',d) #filters lines starting with'from'
print(x)
