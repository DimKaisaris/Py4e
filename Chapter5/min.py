smallest = None
print('Before', smallest)
for num in [9,41,12,3,74,15] :
    if smallest == None :
        smallest = num
    elif num < smallest :
        smallest = num
    print('During',smallest)
print('After','min=', smallest)
