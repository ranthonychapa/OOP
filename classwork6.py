#myStudents = {'s1': 'justus', 's2':'Jemi'}
#myStudents.update({'s3':'Melba','s4':'Jerry'})
#print(myStudents)

#del myStudents['s2']
#print (myStudents)

myStudents = {'s1':{
                       'name':"Justus",
                       'major':"CS",
                       'year':'freshman',
                       'Tcredits':15,
                       'gpa':0.0
                        },
    's2':{
                        'name':"Tony",
                       'major':"CS",
                       'year':'Senior',
                       'Tcredits':127,
                       'gpa':3.7
                        }
    }


print(myStudents)

sid = input("Enter student ID:")
nname = input('Enter student name:')
mmajor = input('Enter student major')
yyear = input('Enter student year')
ttcc = input('Enter Total Credits')
ggpa = input('Enter GPA')

myStudents.update({sid:{
                        'name':nname,
                        'major':mmajor,
                        'year':yyear,
                        'Tcredits':ttcc,
                        'gpa':ggpa,
}})
print(myStudents)

for student_record in myStudents.items():
    print(student_record)
    print('______________________________________________')

