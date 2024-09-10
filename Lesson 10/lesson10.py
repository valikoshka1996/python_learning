#МНОЖИНИ

data = {'Alex', 'Bob', 'Dylan', 6, 10, 6}
# data[0] = 'e' #error
print(data)
data.pop()
data.clear()
print(data) #set()
data.add(7)
print(data) #{7}
data.update(['4', 6, 29])
print(data) #{'4', 29, 6, 7}
data.remove(6)
print(data) #{'4', 29, 7}


nums = [5, 6, 4, 6, 5, 4, 32, 5, 1]
res = set(nums)
print(res) #{32, 1, 4, 5, 6}
word = 'Hello'
print(set(word)) #{'e', 'l', 'o', 'H'}

#frozenset

frozen = frozenset(['a', 'b', 8, 90, 'Set'])
print(frozen) #frozenset({'Set', 'a', 8, 'b', 90})