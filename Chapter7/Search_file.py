fhand = open('Responsibilities and Qualifications.txt')
for line in fhand :
    line=line.strip()
    if line.startswith('*'):
        print(line)
