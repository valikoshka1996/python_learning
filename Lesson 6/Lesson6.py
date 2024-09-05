#MASSIVE

nums =[5, 7, 6, 5.45]
#print(nums, '\n')
nums[0] = 33
#print(nums, '\n')
#print("First eleent:", nums[0], '\n')

#MULTIMASSIVE
nums2 = [5, 5, 7, [5, 6, "Op Op"]]
#print(nums2, '\n')
#print(nums2[3][1])
#print(nums2[-1][0])

#FUNC

nums.append(45)
print("Apend:", nums)
nums.insert(1, False)
print("Insert:", nums)
#nums.extend(nums2)
#print("Extend:", nums)
nums.sort()
print("Sort:", nums)
nums.reverse()
print("Reverse:", nums)
nums.pop()
print("Pop:", nums)
nums.remove(5.45)
print("Remove:", nums)
#nums.clear()
print("Counts 7:", nums.count(7))
print("Len():", len(nums))