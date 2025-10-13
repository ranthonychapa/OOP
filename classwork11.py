file1 = open('test1.txt', 'w')
file1.writelines('Hello world!\n')
file1.writelines('Welcome to OOP Class!\n')
file1.writelines('hope you are enjoying it!\n')

file1.close()

file2 = open('test1.txt', 'r')

for line in file2:
    print(line)
file2.close()

import pickle

d = {'stu1': {'Name': 'John', "Age": "21", "ID": 28},
     'stu2': {'Name': 'Bob', "Age": "99", 'ID': 28},
     'stu3': {'Name': 'Js','Age': '70', 'ID': 28}
}

with open('students.dat', 'wb') as file1:
    pickle.dump(d, file1)
file1.close()

with open('students.dat', 'rb') as file2:
    mydictionary = pickle.load(file2)

print(mydictionary)
file2.close()