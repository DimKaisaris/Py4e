while True:
    line = input('> ')
    if line[0] == '#' :   #[0] means first char '#', it doesnt work in'break'
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
