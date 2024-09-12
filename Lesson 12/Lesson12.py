#FILES

file = open('data/myfile.txt', 'w+') #rewrite a file/ + - create if exist
file.write('Hello World \n')
file.write('End of file \n')
file.close()

file1 = open('data/myfile.txt', 'a') #write to file without loosing data
file1.write('New text')
file1.close()