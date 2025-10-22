class customer:
    def __init__(self):
        self.cid = 0
        self.cname = ''
        self.acc_no = 0
        self.phone = 0
        self.emailID = ''
        self.balance = 0.0
    def add_values_to_customer(self):
        while True:
            try:
                self.cid = int(input('Please Enter Customer ID:'))
                self.cname = input('Please Enter Customer Name:')
                self.acc_no = int(input('Please Enter Account Number:'))
                self.phone = int(input('Please Enter Phone number'))
                self.emailID = input('Please Enter customer email:')
                break
            except ValueError:
                if not self.cid:
                    print ('Error!!!, Please Enter Valid Customer ID!')
                    continue
                if not self.acc_no:
                    print ('Error!!! Please Enter valid account number!!')
                    continue
                if not self.phone:
                    print('Error!! Please Enter a Valid Phone number!!')
                    continue
    def debit_from(self):
        balancetaken = float(input())
        self.balance = self.balance - balancetaken

    def credit_to(self):
        Creditgiven = float(input())
        self.balance = self.balance + Creditgiven

    def display_cust_info(self):
        print(self.cid)
        print(self.cname)
        print(self.acc_no)
        print(self.phone)
        print(self.emailID)
        print(self.balance)

    def display_all(self):
        print(self.cid,': ', self.cname)

#c1 = customer()
#c1.add_values_to_customer()
#c1.display_cust_info()
#c1.debit_from()
#c1.display_cust_info()
#c1.credit_to()
#c1.display_cust_info()
customer_list = []
print('Welcome to our University Balance Management software!')
while True:
    print('Choose one of the following options:')
    print('User Options:')
    print('1.Add Customer to the balance')
    print('2.Charge a customer')
    print('3.Credit to a customer')
    print('4.Display Customer information')
    print('5.Display All Customer Information')
    print('6.Exit')
    print('------------------------------------------')
    try:
        option = int(input('Enter your choice: '))
    except ValueError:
        print("Error!!! Input a valid option!!!")
        continue

    if option == 1:
        new_cust = customer()
        new_cust.add_values_to_customer()
        customer_list.append(new_cust)
    elif option ==2:
        for cust in customer_list:
            if not customer_list:
                print('Error!!! No customers Exists!!!')
                break
            else:
                cust.display_all()
        who_to_charge = int(input("Which of these customers are we charging?"))
        for cust in customer_list:
            if who_to_charge == cust:
                cust.debit_from()
    elif option ==3:
        for cust in customer_list:
            if not customer_list:
                print('Error!!! No customers Exists!!!')
                break
            else:
                cust.display_all()
        who_to_credit = int(input("Which of these customers are we giving credit to?"))
        for cust in customer_list:
            if who_to_credit == cust:
                cust.credit_to()
    elif option ==4:
        for cust in customer_list:
            if not customer_list:
                print('Error!!! No customers Exists!!!')
                break
            else:
                cust.display_all()
        who_to_display = int(input("Which of these customers information do you want to see?"))
        for cust in customer_list:
            if who_to_display == cust:
                cust.display_cust_info()
    elif option ==5:
        for cust in customer_list:
            if not customer_list:
                print('Error!!! No customers Exists!!!')
                break
            else:
                cust.display_cust_info()
    elif option ==6:
        print('Thank you for using our balance management system thank you!')
        break
