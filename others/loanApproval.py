print("Enter True or False for the statement below:")
P = input("Enter 1 if you have served in the armed forces or else enter 0\t")
Q = int(input("Enter you FICO score\t"))

print("Value of P\t", P)
print("Value of Q\t", Q)

if P=="1" and Q>=650:
    print("Your loan is approved with an APR of 2.10")
    print("Thank you for being responsible & serving the nation!")
elif P=="1" and Q<650:
    print("Your loan is approved with an APR of 2.50")
    print("Thank you for serving the nation!")
elif P=="0" and Q>=650:
    print("Your loan is approved with an APR of 3.00")
    print("Thank you for being responsible!")
elif P=="0" and Q<650:
    print("Your loan is not approved")
    print("Please be responsible")
