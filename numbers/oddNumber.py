# programmer: Joseph Kasongo
# program: Odd Numbers From First 100 Natural Numbers
# created on: 09/21/2022 08:09:00
# last modified: 09/21/2022 08:09:00
# version:Python 3.10.7

print("Odd Numbers From the First 100 Natural Numbers:")
for i in range(0,101):
    if(i%2 != 0):
        print(i, end=" \n")

print("Alternate Approach")
for k in range(1,51):
    counter=k
    if counter > 10:
        print("\n")
    print(((2*k)-1), end=" ")

print("Printing odd numbers from first 100 natural numbers using While Loop")
i=1
# When I change to <100, I get up to 199
while (i<51):
    print(((2*i)-1), end=' ')
    i = i+1
print("\n")
print("Alternate way of printing odd numbers from first 100 natural numbers using While Loop")
i=1
while i<=100:
    if(i%2!=0):
        print(i,end=' ')
    i=i+1

i=100
while i>=1:
    if (i%2!=0):
        print(i, end=' ')
    i=i-1
