num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
op= input("Enter the operation which you would wish to use")

if op == "+":
    print("The sum is: ",num1+num2)
elif op == "-":
    print("The Difference is: ",num1-num2)
elif op == "*"or op == "x":
    print("The Product is: ", num1 * num2)
else:
    print("The Quotient is: ", num1/num2)

student_name = input("Enter the student name:")

course1 = int(input("Enter the grade for course 1: "))
course2 = int(input("Enter the grade for course 2: "))
course3 = int(input("Enter the grade for course 3: "))
course4 = int(input("Enter the grade for course 4: "))
course5 = int(input("Enter the grade for course 5: "))

total = course1+course2+course3+course4+course5
print("Your total points is: ", total)

avg = total/5
print(student_name,"'s average grade is: ", avg)
if avg >89:
    print("Grade A")
elif avg >79 and avg<90:
    print("Grade B")
elif avg >69 and avg<80:
    print("Grade C")
elif avg>59 and avg<70:
    print("Grade D")
else:
    print("Grade F")
