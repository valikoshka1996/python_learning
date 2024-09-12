data = input("Your hobby:")

file = open('data/hobbies.txt', 'a+')
file.write(data + '\n')
file.close()