# programmer: Joseph Kasongo
# program:
# created on: 09/24/2022 09:36:00 PM
# last modified: 09/24/2022 09:36:00 PM
# version:1.0.0
# print("Military Time\n")
# time=int(input("Enter time= "))
# if time>=8 and time<18:
#     print("Enjoy Working")
# else:
#     print("Go Home")
# print("\nPrinting odd numbers from first 500 natural numbers:\n")
# for i in range(1,500):
#         if i%2!=0:
#             print(i, end=' ')
# print("\nPrinting natural numbers between 100 and 200:\n")
# i=100
# while i<=200:
#     print(i)
#     i +=1
# print("\nPrinting Hello 'Name' \n")
# name=str(input("Enter your name: "))
# print("Hello "+name)

import math
print("\nChoose one operation:\n")
print("1.Compute area of a circle\n2.Compute area of a rectangle\n3.Compute area of a triangle\n4.Compute area of a Rhombus\n5.Compute the square root of a number\n")
choice=input("Enter operation number: ")
while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5":
    print("Invalid choice, enter again")
    choice=input("Enter the right operation number: ")
print("We move onto the next step")
