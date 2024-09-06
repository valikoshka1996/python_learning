#TEXT
word = list('Hello World')
word[0] = "I"
print(word.count("o"))
word.append('!')
print(word)
result = ''.join(word)
print("result:", result)
print(result.upper())
print(result.islower())


text = 'football, basketball, skate'
hobbies = text.split(',')
#print(hobbies)

for i in range(0, len(hobbies)):
	hobbies[i] = hobbies[i].capitalize()

result = ",".join(hobbies)
print(result)


#INDEXES 
lis = [5, 6, 3, "Hell", "O", [32,3]]
print(lis[0:2]) #[5, 6]
print(lis[2:]) #[3, 'Hell', 'O', [32, 3]]
print(lis[2:-1]) #[3, 'Hell', 'O']
print(lis[:-1]) #[5, 6, 3, 'Hell', 'O']
print(lis[0::2]) #[5, 3, 'O']
print(lis[::-1]) #[[32, 3], 'O', 'Hell', 3, 6, 5]
print(lis[:-4:-1]) #[[32, 3], 'O', 'Hell']