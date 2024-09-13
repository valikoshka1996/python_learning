#EXCEPTIONS
num = None

while num is None:
	try:
		num = int(input("Enter number"))
		num += 5
		print(num)
	except ValueError:
		print("It isn't number")
	
