first = open('new_file.txt','w')
p = 0
for i in range(50):
	i = i + p
	first.write(str(i))
	first.write('\n')

first.close()

first_open = open('new_file.txt','r')
lines = first_open.read()

print(lines)	