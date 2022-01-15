sum = 0
count = 0
print('Start')
while True :
    sval = input ('Enter a number: ')
    if sval == 'done' :
        break
    try:
        value = float(sval)
    except:
        print("Invalid Input")
        continue
    sum = sum + value
    count = count +1
print('End')
print('n=',count,'Sum=',sum,'Average=', sum/count)
