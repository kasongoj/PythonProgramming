"""
programmer: Joseph Kasongo
program: natural numbers
version:1.0.0
created on: 09/26/2022 08:04:00
last modified: 09/30/2022 08:17:00

"""
print("Welcome to mathematical operations")
print("1. Odd Numbers\n"
      "2. Even Numbers\n"
      "3. Prime Numbers\n"
      "4. Perfect Numbers\n"
      "5. Palindrome Numbers")
choice=int(input("Select the operation by choosing a number:\t"))
if choice==1:
    print("Odd Numbers From the First 100 Natural Numbers:")
    for i in range(0,101):
        if(i%2 != 0):
            print(i, end=" ")

    # print("Alternate Approach")
    # for k in range(1,51):
    #     counter=k
    #     if counter > 10:
    #         print("\n")
    #         print(((2*k)-1), end=" ")

    print("\nPrinting odd numbers from first 100 natural numbers using While Loop")
    i=1
    # When I change to <100, I get up to 199
    while (i<51):
        print(((2*i)-1), end=' ')
        i = i+1
# print("\n")
# print("Alternate way of printing odd numbers from first 100 natural numbers using While Loop")
# i=1
# while i<=100:
#     if(i%2!=0):
#         print(i,end=' ')
#     i=i+1

# i=100
# while i>=1:
#     if (i%2!=0):
#         print(i, end=' ')
#     i=i-1
elif choice==2:
    print("Printing even numbers using For Loop")
    for i in range(2,101):
        if i%2==0:
            print(i, end=' ')
    print("\nPrinting even numbers using While Loop")
    i=2
    while i<=100:
        if i%2==0:
            print(i, end=' ')
        i +=1
elif choice==3:
    print("\nPrinting prime numbers from first 100 natural numbers")
    for i in range(1,101):      # iterating for numbers between 2 and n/2+1
        counter=0     # initializing counter variable to 0
        for j in range(2,int(i/2)+1):       # checking number of divisors for a number
            if i%j==0:      # check for remainder is 0
                counter+=1      # increase the counter if you find a divisor
        if counter==0:          # decision to see if counter is 0 i.e no divisors
            print(i, end=' ')   # printing if the number is prime
elif choice==4:
    print("\nPrinting perfect numbers from first 100 natural numbers")
    for i in range(1, 51):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            print(i,end=" ")
else:
    print("Palindrome numbers from first 100 natural numbers")
    number=int(input("Enter a number: "))
    originalNumber=number
    rev=0
    while number>0:
        rem=int(number%10)
        rev=int(rev*10+rem)
        number=int(number/10)
    if originalNumber==rev:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")





