""""
programmer: Joseph Kasongo
program: assignment 2
python version: Python 3.8.2
created on: 09/24/2022 09:36:00 PM
last modified: 09/24/2022 09:36:00 PM
version:1.0.0
"""
print("Question1: Military Time\n")
time=int(input("Enter time= "))
if time>=8 and time<18:
    print("Enjoy Working")
else:
    print("Go Home!")
print("\nQuestion3: Printing odd numbers from first 500 natural numbers:\n")
for i in range(1,500):
        if i%2!=0:
            print(i, end=' ')
print("\n")
print("\nQuestion3: Printing natural numbers between 100 and 200:\n")
i=100
while i<=200:
    print(i,end=" ")
    i +=1
print("\n")
print("\nQuestion6: Printing Hello 'Name' \n")
name=str(input("Enter your name: "))
print("Hello "+name)

import math
print("\nQuestion8: Choose one operation:\n")
print("1.Compute area of a circle\n2.Compute area of a rectangle\n3.Compute area of a triangle\n4.Compute area of a Rhombus\n5.Compute the square root of a number\n")
choice=input("Select an operation by entering a number from the options above: ")
while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5":
    print("Invalid choice, enter again")
    choice=input("Enter the right operation number: ")
if choice=="1":
    print("Provide the value of the radius\n")
    radius=int(input("radius= "))
    areaCircle=math.pi * radius * radius
    print("Area of the circle is ",areaCircle)
elif choice=="2":
    print("Provide the value of the width and the length\n")
    width=int(input("width= "))
    length=int(input("length= "))
    areaRect=width*length
    print("Area of the rectangle is ",areaRect)
elif choice=="3":
    print("Provide the value of the base and the height\n")
    base=int(input("base= "))
    height=int(input("height= "))
    areaTr=base*height*0.5
    print("Area of the triangle is ",areaTr)
elif choice=="4":
    print("Provide the value of the diagonals\n")
    diagFirst=int(input("diagonal1= "))
    diagTwo=int(input("diagonal2= "))
    areaRh=diagFirst*diagTwo*0.5
    print("Area of the rhombus is ",areaRh)
else:
    number=int(input("Enter a number: "))
    print(f"The square root of {number} is ",math.sqrt(number))
