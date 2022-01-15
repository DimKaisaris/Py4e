fhand = open('Responsibilities and Qualifications.txt')
for line in fhand :
    line=line.strip() # so to delete blank(\n) lines
    if line.startswith('*'):
        print(line)
fhand = open('Responsibilities and Qualifications.txt')  #we need to reopen to run the code
char = fhand.read()
print(len(char))
print(char[:15])
