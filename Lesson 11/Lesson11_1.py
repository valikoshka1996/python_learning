def minimal(l):
	minX = l[0]
	for i in l:
		if i < minX:
			minX = i
	
	return(minX)



nums1 = [3, -222, 5, 2, 23, 53, 34, 34, 2332, 2, 6, 3, 34, 12]
nums2 = [23, 2, 12, 5, 34, -9, 6, 23, 11, -323]

minimal1 = minimal(nums1)
minimal2 = minimal(nums2)

if minimal1 < minimal2:
	print(minimal1)
else:
	print(minimal2)


#LAMBDA FUNC
func = lambda x, y: x * y

print(func(3, 2))

user_count = int(input("Enter count for numbers"))

i = 0
numbers = []
while i < user_count:
	text = "Enter " + str(i) + " number"
	numbers.append(input(text)) 
	i += 1

print("Minimal number:", minimal(numbers))
