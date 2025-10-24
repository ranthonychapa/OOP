#problem 1
print("Weclome to OOP Class")
name = input("Enter your Name: ")
print("Welcome ", name)
#problem 2
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
#problem 3
wages = int(input("Enter the wages"))
hours = int(input("Enter your hours: "))
days = int(input("Enter your days: "))
monthly_wages = wages*hours*days
print(monthly_wages)

