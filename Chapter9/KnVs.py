jjj={'Chuck':3, 'Fred':42, 'Jan':100 }
print(jjj)
print(list(jjj))  #convert to a list with the keys
print(jjj.keys()) #or use method .keys()
print(jjj.values()) #method for values   .values()
print(jjj.items())  #method .items() gives a list of key-value pair(tuple)
print(len(jjj.items()))

for k,v in jjj.items(): #two iteration variables
    print(k,v)
