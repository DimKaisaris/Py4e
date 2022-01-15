smallest = None
largest = None
while  True :
    svalue = input ('Enter a number: ')
    if svalue == 'done' :
        break
    try:
        value = float(svalue)
    except:
        print('Invalid Input')
        continue
    if smallest is None :
        smallest = value
        largest = value
    elif value < smallest :
        smallest = value
    elif value > largest :
        largest = value
print('Maximum is', largest)
print('Minimun is', smallest)
