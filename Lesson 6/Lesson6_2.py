#MASSIVES AND LOOPS
nums =[5,4,3,4,7,5,65]

for el in nums:
	res = el ** 2
	print(res)

#your hobbies

user_count_hobby = int(input("Enter count fo hobbys"))

i = 0
hobby =[]
while i < user_count_hobby:
	text = "Enter " + str(i) + " hobby"
	hobby.append(input(text)) 
	i += 1
print("Check your hobbies:", hobby)