class Student:
    def __init__(self):#constructor function
        self.SID=''
        self.stu_name=''
        self.major=''
        self.gpa=0.0
        self.dob = ''
        self.courses = []
    def add_student(self):
        self.SID = input('Enter the SID:')
        self.stu_name = input('Enter the name:')
        self.major = input('Enter the major')
        self.gpa = float(input("Enter the GPA"))
        self.dob = input('Enter the DOB')
        self.courses = []
    def register_courses(self, cc1):
        self.courses.append(cc1)

    def edit_student(self):
        self.SID = input('Enter the SID:')
        self.stu_name = input('Enter the name:')
        self.major = input('Enter the major')
        self.gpa = float(input("Enter the GPA"))
    def display_student(self):
        print('Stu ID:', self.SID)
        print('Stu Name:',self.stu_name)
        print('Major:',self.major)
        print('GPA:',self.gpa)
        print('DOB:', self.dob)
        for x in self.courses:
            print('Registered Courses:', x.cname)

class Course:
    def __init__(self, x, y):
        self.cid = x
        self.cname = y
    def add_course(self):
        self.cid = input('Enter course ID:')
        self.cname = input("Enter Course name")

#main code
print('Welcome to our University Database!')
#while True:
    #print('Choose one of the following options:')
   # print('1.Add a student to the database')
    #print('2.Edit student information in the database')
   # print('3. Display student information')
    #try:
     #   option = int(input('Option Selected:'))
   # except ValueError:
    #    print ('Error! Please input a valid option!')
    ##if option
s1 = Student()
s2 = Student()
s3 = Student()
s1.add_student()
s2.add_student()
s3.add_student()
s1.display_student()
s2.display_student()
s3.display_student()

c1 = Course('CS1233', 'OOP')
c2= Course('CS2423', 'Web Application')
c3 =Course('MTH2134', 'Discrete Math')

s1.register_courses(c1)
s1.register_courses(c2)
s2.register_courses(c1)
s2.register_courses(c2)
s3.register_courses(c2)

s1.display_student()
s2.display_student()
s3.display_student()