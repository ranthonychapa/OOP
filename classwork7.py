Projects = {"p1": {
        "Project_title": [],
        "managers": [],
        "start_date": "Sep 22nd, 2025",
        "enda_date":[],
        "sponsor": [],
        "budget":[],
        "technologies": [],
        "team_members": [],
        }}

#1. Project Initiation
#2. Project closure
#3. Project progress update
#4. Print a specific Project
#5. Print all projects
#6. Quit application
print ('Welcome to our project management software!')
while 1:
    print('1. Project Initiation')
    print('2. Project closure')
    print('3. Project progress update')
    print('4. Print a specific project')
    print('5. Print ALL projects')
    print('6. Quit application')
    try:
        option = int(input('Please select one of the following choices:'))
    except ValueError:
        print('Error! Please input a valid option')
        continue
    if option ==1:
        managers = []
        tech = []
        team = []
        pid = input("Enter Project ID:")
        pt = input("Enter Project Title")
        try:
            n = int(input("how managers you want to enter:"))
        except ValueError:
            print('Error! Please input a number')
            continue
        for i in range(0,n):
            managers.append(input("Enter Manager's Name:"))
        sd = input("Enter Start Date: ")
        ed = input("Enter End Date: ")
        spon = input("Enter the Sponsor: ")
        bdg = input("Enter the Budget: ")
        try:
            n = int(input("Enter how many technologies you want to enter"))
        except ValueError:
            print('Error! Please input a number')
            continue
        for i in range(0,n):
            tech.append(input("Enter the Technology:"))
        n = int(input("Enter how many Team Members you want to enter"))
        for i in range(0,n):
            team.append(input("Enter the Team Member's Name:"))
        Projects.update({pid:{
            "Project_title":pt,
            "managers": managers,
            "start_date": sd,
            "end_date": ed,
            "sponsor": spon,
            "budget": bdg,
            "technologies": tech,
            "team_members": team
            }})
    elif option ==2:
        print("Current Project records:")
        for Pid in Projects:
            print(Pid)
            print("---------------------------------------------")
        pdel = input("Which of the following Projects would you like to close?")
        if pdel in Projects:
            del Projects[pdel]
            print("Record deleted.")
        else:
            print("Project info not found.")
    elif option == 3:
        print("Current Employee records:")
        for Pid in Projects:
            print(Pid)
            print("---------------------------------------------")
        ProjID = input("Enter Employee information to be replaced:")
        if ProjID in Projects:
            managers = []
            tech = []
            team = []
            pid = input("Enter Project ID:")
            pt = input("Enter Project Title")
            n = int(input("how managers you want to enter:"))
            for i in range(0, n):
                managers.append(input("Enter Manager's Name:"))
            sd = input("Enter Start Date: ")
            ed = input("Enter End Date: ")
            spon = input("Enter the Sponsor: ")
            bdg = input("Enter the Budget: ")
            n = int(input("Enter how many technologies you want to enter"))
            for i in range(0, n):
                tech.append(input("Enter the Technology:"))
            n = int(input("Enter how many Team Members you want to enter"))
            for i in range(0, n):
                team.append(input("Enter the Team Member's Name:"))
            Projects.update({pid: {
                "Project_title": pt,
                "managers": managers,
                "start_date": sd,
                "end_date": ed,
                "sponsor": spon,
                "budget": bdg,
                "technologies": tech,
                "team_members": team
            }})
            print("Record updated.")
        else:
            print("Project info not found.")
    elif option ==4:
        print("Current Project records:")
        for Pid in Projects:
            print(Pid)
            print("---------------------------------------------")
        pprint = input("Which of the following Projects would you like to print?")
        if pprint in Projects:
            print(Projects[pprint])
        else:
            print("Project info not found.")
    elif option == 5:
        for Project_record in Projects.items():
            print(Project_record)
            print('______________________________________________')
    elif option == 6:
        break
    else:
        print('ERROR: Please input a valid option')