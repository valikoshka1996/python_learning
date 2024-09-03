# IF, ELSE, ELIF

num = int(input("Enter a number"))

#EXAMPLE BASIC IF
# ==, !=, <, >, <=, >=
if num >= 5:
	print("Bigger than 5")
	if num >= 100:
		print("birreg than 100")
print("All")
 
#BOOLEAN IF

isHappy = True
if isHappy:
	print("He is happy")

isHappy = False
if not isHappy:
	print("He isn't happy")

#EXAMPLE IF ELSE

engine = int(input("Enter capacity"))
if engine <= 3:
	print("Engine is sucks")
else:
	print("Engine is strong")

#EXAMPLE ELIF

tank = int(input("Enter capacity"))
if tank <= 3:
	print("Tank is sucks")
elif tank >=5:
	print("Tank is strong")
else:
	print("Not enough")

#EXAMPLE CONSTRUCTED IF

inp = int(input("Enter a number"))
isCar = True
if  inp >= 1 and isCar:
	print("Yes, that fit and")

if  inp >= 1 or not isCar:
	print("Yes, that fit or")