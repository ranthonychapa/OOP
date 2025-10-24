class customer:
    def __init__(self):
        self.cid = 0
        self.cname = ''
        self.acc_no = 0
        self.phone = 0
        self.emailID = ''
        self.balance = 0.0
        self.credit_card = []
        self.debit_card = 0
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
        print(self.credit_card)
        print(self.debit_card)

    #def display_all(self):
        #for x in customer:
           # print(x.cid,':', x.cname)

class Card:
    def __init__(self):
        self.type = ''
        self.c_no = 0
        self.cvv = 0
        self.expiry_date = ''
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
        print(self.credit_card)
        print(self.debit_card)
customer_list = []
C1 = customer()
C1.add_values_to_customer()
C1.display_cust_info()
C1.debit_from()
C1.display_cust_info()
C1.credit_to()
C2 = customer()
C2.add_values_to_customer()
C2.credit_to()
customer_list.append(C1)
customer_list.append(C2)
