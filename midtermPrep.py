"""
programmer: Joseph Kasongo
program: midterm preparation package
version:1.0.0
created on: 10/06/2022 04:09:00 PM
last modified: 10/06/2022 04:11:00 PM

"""
print("Odd numbers using For Loop\n")
for i in range(1,100,2):
    print(i, end=" ")
print("\nOdd numbers using For Loop")
for i in range(1,101):
    if i%2!=0:
        print(i, end=" ")
print("\nOdd numbers using While Loop")
i=1
while i<=50:
    n=(2*i)-1
    print(n, end=" ")
    i+=1
print("\nOdd numbers using While Loop")
i=1
while i<=100:
    if i%2!=0:
        print(i, end=" ")
    i+=1

print("\nEven numbers")
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")
print("\nEven numbers")
i=2
while i<=100:
    if i%2==0:
        print(i, end=" ")
    i+=1

print("\nPrime Numbers")
for p in range(2,101):
    counter=0
    for q in range(2,int((p/2)+1)):
        if p%q==0:
            counter+=1
    if counter==0:
        print(p, end=" ")

print("\nPerfect numbers")
for e in range(1,101):
    sum=0
    for f in range(1,e):
        if e%f==0:
            sum+=f
    if sum==e:
        print(e, end=" ")

print("\nPalindrome")

number=int(input("Number= "))
originalNumber=number
reverse=0
while number>0:
    remainder=int(number%10)
    reverse=int(reverse*10+remainder)
    number=int(number/10)
if reverse==originalNumber:
    print("is a palindrome")
else:
    print("not a palindrome")

print("\nArmstrong")
number=int(input("Number= "))
tempNumber=number
sum=0
while tempNumber>0:
    digit=int(tempNumber%10)
    sum+=digit**3
    tempNumber/=10
if number==sum:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")


