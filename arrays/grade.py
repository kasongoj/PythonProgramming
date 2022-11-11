"""
programmer: Joseph Kasongo
Program: Array illustration
created on:
last updated:
"""

grade = [15, 20, 30, 23, 11]

print(grade)
index = int(input("Which assignment grade do you want to know\t"))
print("The grade you have received in assignment 1 is ", grade[index-1])

for i in range(0, len(grade)):
    grade[i] = grade[i] + 2

print("Displaying the updated grade\n", grade)

