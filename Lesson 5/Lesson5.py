#BASIC FOR

for i in range(11):
	print("I:", i)

print('\n')

#range(for, to, step)

for y in range(5, 16, 2):
	print("Y:", y)

print('\n')

word = 'Hello Worldy'

for i in word:
	print(i)

print('\n')

for i in word:
	if i == 'y':
		print('There is У letter in da text')
print('\n')

#WHILE
i = 0
while i <= 10: #<, >, <>, >=, <=
	print("While I:", i)
	i += 1

print('\n')
work = True

while work:
	print("Listen")
	user_input = input("Enter word Stop")
	if user_input == "Stop":
		work = False
print("While loop is done")

#OPERATORS
for i in range(1, 11):
	if i == 7:
		break
	print("Element:", i)

for i in range(1, 11):
	if i % 2 == 0:
		continue
	if i == 7:
		break
	print("Element:", i)

#ELSE in FOR

for i in "Hallo Freunde":
	if i == "r":
		print("Done")
		break
else:
	print("Not found")

