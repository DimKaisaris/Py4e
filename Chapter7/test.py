fhand = open('Responsibilities and Qualifications.txt')
char = fhand.read()
print(len(char))
print(char[:15])
for line in fhand : #it doesnt work. see test2 for solution
    if line.startswith('*'):
        print(line)
