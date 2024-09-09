#LIBRARIES

person = {'name':'Alex', 'age': 12, 5: 12, True: 'This text is true', (3, 5): 99}
print(person) #{'name': 'Alex', 'age': 12, 5: 12, True: 'This text is true', (3, 5): 99}
print(person['age']) #12
print(person[True]) #This text is true

person[5] = 'Twelve'
print(person[5]) #Twelve

person1 = dict(name='Alex', age=15)
print(person1['name']) #Alex

for key in person:
	print(key)

print(person.items())

for key, values in person.items():
	print(key, values, sep='-')

for el in person.values():
	print(el)

print(person.get('name')) #Alex
#person.clear()
#print(person)
#person.popitem()
#print(person)
#person.pop(5)
#print(person)
person['bio'] = 'graphy'
print(person) #{'name': 'Alex', 'age': 12, 5: 'Twelve', True: 'This text is true', (3, 5): 99, 'bio': 'graphy'}
