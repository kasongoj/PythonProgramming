print("Welcome to Grade Assignment \n")
name = input("Student Name: ")
ID = input("Student SC ID: ")
assignment = int(input("Enter your % on assignment component of grade evaluation= "))
lab = int(input("Enter your % on lab component of grade evaluation= "))
reading = int(input("Enter your % on reading component of grade evaluation= "))
quiz = int(input("Enter your % on quizzes component of grade evaluation= "))
midterm = int(input("Enter your % on midterm component of grade evaluation= "))
project = int(input("Enter your % on project component of grade evaluation= "))
total = assignment+lab+reading+quiz+midterm+project
if total >= 94:
    print("Letter Grade: A")
    print("Grade point: 4.000")
    print("Excellent Performance "+name)
elif total > 90:
    print("Letter Grade: A-")
    print("Grade point: 3.667")

elif total > 87:
    print("Letter Grade: B+")
    print("Grade point: 3.333")

elif total > 84:
    print("Letter Grade: B")
    print("Grade point: 3.000")
    print("Good Performance "+name)
elif total > 80:
    print("Letter Grade: B-")
    print("Grade point: 2.667")

elif total > 77:
    print("Letter Grade: C+")
    print("Grade point: 2.333")

elif total > 74:
    print("Letter Grade: C")
    print("Grade point: 2.000")
    print("Average Performance "+name)
elif total > 70:
    print("Letter Grade: C-")
    print("Grade point: 1.667")

elif total > 65:
    print("Letter Grade: D+")
    print("Grade point: 1.333")

elif total > 60:
    print("Letter Grade: D")
    print("Grade point: 1.000")
    print("Unsatisfactory Performance "+name)
elif total >= 55:
    print("Letter Grade: D-")
    print("Grade point: 0.667")

else:
    print("Letter Grade: F")
    print("Grade point: 0.000")
    print("Failing Performance "+name)
