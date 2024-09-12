file = open('data/hobbies.txt', 'r') #read files
data = file.read()

print(data)
for line in file:
	print(line)


file.close()