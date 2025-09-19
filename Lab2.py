myEmployees = {}
#netpay = Basic pay + allowance
#grosspay = Net pay - (Deductions + Taxes)
print('Welcome employee database:')
while 1:
    print('Choose one of the following choices:')
    print("1. Add an employee to the database")
    print('2. Delete an employee from the database')
    print('3. Replace an employee from the database')
    print('4. Print the employee database')
    print('5. Quit')

    try:
        option = int(input())
    except ValueError:
        print("Error! Please enter a valid option!")
        continue
    if option == 1:
        Ename = input("Enter new Employee name:")
        BasPay = int(input('Enter new Base Pay:'))
        APay = int(input('Enter new Allowances:'))
        Dedct = int(input('Enter new deductions'))
        Taxes = float(BasPay *0.0825)
        Netpay = BasPay + APay
        Grspay = Netpay - (Dedct + Taxes)
        myEmployees.update({Ename: {
            'Base Pay:': BasPay,
            'Allowances:': APay,
            'Deductions:': Dedct,
            'Taxes:': Taxes,
            'Netpay:': Netpay,
            'Grosspay:': Grspay,
        }})
    elif option == 2:
        print("Current Employees records:")
        for EmpID in myEmployees:
            print(EmpID)
            print("---------------------------------------------")
        Empdel = input("Enter student ID to delete:")
        if Empdel in myEmployees:
            del myEmployees[Empdel]
            print("Record deleted.")
        else:
            print("Employee info not found.")
    elif option == 3:
        print("Current Employee records:")
        for EmpID in myEmployees:
            print(EmpID)
            print("---------------------------------------------")
        EmpID = input("Enter Employee information to be replaced:")
        if EmpID in myEmployees:
            Ename = input("Enter new Employee name:")
            BasPay = int(input('Enter new Base Pay:'))
            APay = int(input('Enter new Allowances:'))
            Dedct = int(input('Enter new deductions'))
            Taxes = float(BasPay * 0.0825)
            Netpay = BasPay + APay
            Grspay = Netpay - (Dedct + Taxes)
            myEmployees.update({Ename: {
                'Base Pay:': BasPay,
                'Allowances:': APay,
                'Deductions:': Dedct,
                'Taxes:': Taxes,
                'Netpay:': Netpay,
                'Grosspay:': Grspay,
            }})
            myEmployees[EmpID] = {
                'Base Pay: ': BasPay,
                'Allowances:': APay,
                'Deductions: ': Dedct,
                'Taxes:': Taxes,
                'Netpay:': Netpay,
                'Grosspay': Grspay,
            }
            print("Record updated.")
        else:
            print("Employee info not found.")
    elif option == 4:
        for employee_record in myEmployees.items():
            print(employee_record)
            print('______________________________________________')
    elif option ==5:
        break
    else:
        print('ERROR: Please input a valid option')