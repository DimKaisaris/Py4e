largest = None
print('Before', largest)
for value in [9,41,12,3,74,15] :
    if largest == None :
        largest = value
    elif value > largest :
        largest = value
    print('During', largest)
print('After','max=', largest)
