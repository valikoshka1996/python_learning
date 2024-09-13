#EXCEPTION EXAMPLE

try:
	a = 10
	b = int(input("Enter a num"))
	
	print(a / b)
except ValueError:
	print("It isn't number")
#except ZeroDivisionError:
#	print("Zero div")

#except Exception:
#	print("Something went wrong")
else: 
	print('You are cool')
finally:
	print("You request has been done")