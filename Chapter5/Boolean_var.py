found = False
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True      # we can put break after found
    print(found, value)
print('After', found)     # if we just want to search and know if a value was found 
