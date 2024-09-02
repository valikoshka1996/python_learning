#BASIC EXAMPLE 

a = input("Enter first word")
b = input("Enter second word") #default "string" type 

print(a + b)

#CHANGING TYPES EXAMPLE (FROM STR TO INT)
a = int(input("Enter first int"))
b = input("Enter second int") 

print(a + int(b))


#CHANGING TYPES EXAMPLE (FROM STR TO FLOAT)
a = float(input("Enter first float"))
b = input("Enter second float") 

print(a + float(b))



#SHORT NOTATION
a = int(input("Enter first int"))
b = int(input("Enter second int"))

cache = a

a += b

print("Sum", a)

a = cache

a /= b

print("Dil", a)

a = cache

a *= b

print("Mnog", a)
