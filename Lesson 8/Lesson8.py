#Кортеджі non editable

data = (5, 6, 7, "tezt", [5,6,7], (1,5,"Haha"))
print(data) #(5, 6, 7, 'tezt', [5, 6, 7], (1, 5, 'Haha'))
print(data[3]) #tezt
print(data[4][1]) #6
print(data.count(5)) #1

info = 6, 7, 8, 9

print(info) #(6, 7, 8, 9)

info1 = 5
print(info1) #5

for i in data:
	print("For cortage:", i)

nums = [5, 6, (5, 6)]

edit = tuple(nums)
print(edit) #(5, 6, (5, 6))

