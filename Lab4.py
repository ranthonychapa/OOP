import pickle
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
                cust_id = int(input('Please Enter Customer ID:'))
                if any(c_id.cid == cust_id for c_id in customer_list):
                    print('Error!!! Customer ID Already Exists!!')
                    continue
                self.cid = cust_id
                self.cname = input('Please Enter Customer Name:')
                self.acc_no = int(input('Please Enter Account Number:'))
                self.phone = int(input('Please Enter Phone number'))
                self.emailID = input('Please Enter customer email:')
                print('----------------------------------------------')
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
                print('----------------------------------------------')
    def Edit_customer(self):
        while True:
            try:
                self.phone = int(input('Please Enter Phone number'))
                self.emailID = input('Please Enter customer email:')
                print('----------------------------------------------')
                break
            except ValueError:
                if not self.phone:
                    print('Error!! Please Enter a Valid Phone number!!')
                    continue
                print('----------------------------------------------')
    def debit_from(self):
        charge = float(input('How much is the Customer withdrawing today?'))
        self.balance = self.balance - charge
        print('----------------------------------------------')

    def credit_to(self):
        Creditgiven = float(input('How much is the Customer Depositing today?'))
        self.balance = self.balance + Creditgiven
        print('----------------------------------------------')

    def display_cust_info(self):
        print('Customer ID:',self.cid)
        print('Customer Name:',self.cname)
        print('Account Number:',self.acc_no)
        print('Phone Number:',self.phone)
        print('Customer Email:',self.emailID)
        print('Customer Balance:',self.balance)
        if self.credit_card:
            print('Customer Credit Cards:', [card.c_no for card in self.credit_card])
        else:
            print('Customer Credit Cards: None')
        if self.debit_card:
            print('Customer Debit Card:', self.debit_card.c_no)
        else:
            print('Customer Debit Card: None')
        print('----------------------------------------------')

    def fund_transfer(self, other_customer):
        try:
            amount = float(input(f'How much is {self.cname} transferring to {other_customer.cname}? '))
            if amount > self.balance:
                print("Error!! Insufficient funds.")
            else:
                self.balance -= amount
                other_customer.balance += amount
                print(f'{user.cname} Transferred [funds] {account.cname} successfully!')
        except ValueError:
            print("Error!! Please enter a valid amount.")

    def assign_card(self, card):
        if card.type == "Debit Card":
            if self.debit_card:
                print("Error!! This customer already has a debit card.")
                print('--------------------------------------------------')
            else:
                self.debit_card = card
                print(f'{user.cname} assigned {card.c_no} successfully!')
        elif card.type == "Credit Card":
            self.credit_card.append(card)
            print(f'{user.cname} assigned {card.c_no} successfully!')
            print('----------------------------------------------')


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
    def add_values_to_card(self):
        while True:
            try:
                print('Which Type of card would you like to apply for? ')
                print('1. Debit Card  OR  2. Credit Card')
                new_card = int(input('Please Enter Card Type:'))
                if new_card ==1:
                    self.type = 'Debit Card'
                elif new_card ==2:
                    self.type = 'Credit Card'
                else:
                    print('Error!!!, Please choose between options 1 or 2!!!')

                crd_id = int(input('Please Enter Card Number:'))
                if any(c_id.c_no == crd_id for c_id in card_list):
                    print('Error!!! Card Number Already Exists!!')
                    continue
                self.c_no = crd_id
                self.cvv = int(input('Please Assign CVV:'))
                self.expiry_date = input('Please Enter Expiry date:')
                print('----------------------------------------------')
                break
            except ValueError:
                if not new_card:
                    print('Error!!!, Please Choose between option 1 or 2!!!')
                    continue
                if not self.c_no:
                    print ('Error!!!, Please Enter Valid Card Number!')
                    continue
                if not self.cvv:
                    print ('Error!!! Please Enter valid CVV!!')
                    continue
                print('----------------------------------------------')
    def charge_card(self):
        balancetaken = float(input('How Much are we charging the customer today?:'))
        self.balance = self.balance - balancetaken
        print('----------------------------------------------')

    def credit_to_card(self):
        Creditgiven = float(input('How much are we crediting the customer today?:'))
        self.balance = self.balance + Creditgiven
        print('----------------------------------------------')

    def display_card_info(self):
        print('Card Type:',self.type)
        print('Card Number:',self.c_no)
        print('CVV:',self.cvv)
        print('Expiry Date:',self.expiry_date)
        print('Balance:',self.balance)
        print('----------------------------------------------')

customer_list = []
card_list = []
#C1 = customer()
#C1.add_values_to_customer()
#C1.display_cust_info()
#C1.debit_from()
#C1.display_cust_info()
#C1.credit_to()
#C2 = customer()
#C2.add_values_to_customer()
#C2.credit_to()
#customer_list.append(C1)
#customer_list.append(C2)
#DC = Card()
#CC1 = Card()
#DC.add_values_to_card()
#DC.credit_to_card()
#DC.charge_card()
#DC.display_card_info()
#CC1.add_values_to_card()
#CC1.display_card_info()
#C1.debit_card = DC
#C1.credit_card.append(CC1)
#C1.display_cust_info()
print('Welcome to our Banking Management system!')
while True:
    print('Choose one of the following options:')
    print('Customer Based Options:')
    print('1. Add a Customer to the database')
    print('2. Edit Customer information in the database')
    print('3. Display Customer information')
    print('4. Deposit Funds into Account')
    print('5. Charge Account')
    print('6. Transfer Funds between Customers')
    print('------------------------------------------')
    print('Card Options:')
    print('7. Add a new card to the database')
    print("8. Assign Card to customer")
    print('9. Display Card Information')
    print('--------------------------------------------')
    print('Miscellaneous Functions:')
    print('10. Save to file')
    print('11. Exit')
    print('-------------------------------------------')
    try:
        option = int(input('Option Selected:'))
    except ValueError:
        print ('Error! Please input a valid option!')
        continue
    if option == 1:
        new_user = customer()
        new_user.add_values_to_customer()
        customer_list.append(new_user)
    elif option == 2:
        if not customer_list:
            print('Error!! No customers currently exists!!')
        else:
            print('Enrolled Customer:')
            for user in customer_list:
                user.display_cust_info()

            while True:
                try:
                    User_select = int(input("Which Customer would you like to Edit? Enter Customer ID: "))
                    user_searched = 0
                    for user in customer_list:
                        if user.cid == User_select:
                            user_searched = user
                            break
                    if user_searched:
                        user_searched.Edit_customer()
                        print("Customer info updated")
                        print('_____________________________________')
                        break
                    else:
                        print('Error!!! Customer ID not found')
                        print('_____________________________________')
                        break
                except ValueError:
                    print("Please enter a valid number.")
    elif option ==3:
        if not customer_list:
            print ('Error!! No customers exist yet!!')
        else:
            for user in customer_list:
                user.display_cust_info()
    elif option ==4:
        if not customer_list:
            print('Error!! No customers currently exists!!')
        else:
            print('Enrolled Customer:')
            for user in customer_list:
                user.display_cust_info()

            while True:
                try:
                    User_select = int(input("Which Customer acc would you like to deposit funds into"))
                    user_searched = 0
                    for user in customer_list:
                        if user.cid == User_select:
                            user_searched = user
                            break
                    if user_searched:
                        user_searched.credit_to()
                        print("Deposit complete")
                        print('_____________________________________')
                        break
                    else:
                        print('Error!!! Customer ID not found')
                        print('_____________________________________')
                        break
                except ValueError:
                    print("Please enter a valid number.")
    elif option ==5:
        if not customer_list:
            print('Error!! No customers currently exists!!')
        else:
            print('Enrolled Customer:')
            for user in customer_list:
                user.display_cust_info()

            while True:
                try:
                    User_select = int(input("Which Customer acc would you like to bill"))
                    user_searched = 0
                    for user in customer_list:
                        if user.cid == User_select:
                            user_searched = user
                            break
                    if user_searched:
                        user_searched.debit_from()
                        print("Charging account complete")
                        print('_____________________________________')
                        break
                    else:
                        print('Error!!! Customer ID not found')
                        print('_____________________________________')
                        break
                except ValueError:
                    print("Please enter a valid number.")
    elif option ==6:
        if not customer_list:
            print("Error!! You must have at least one customer to be able to transfer funds.")
        else:
            print("Enrolled Customer:")
            for user in customer_list:
                user.display_cust_info()
            try:
                user_id = int(input('Which customer is transferring funds?:'))
                user = next((u for u in customer_list if u.cid == user_id), None)
                if not user:
                    print("Error!! Customer not found.")
                else:
                    print("Available Accounts to transfer funds to:")
                    for account in customer_list:
                        account.display_cust_info()

                    acc_id = int(input('Which account is the funds being transferred to?:'))
                    account = next((acc for acc in customer_list if acc.cid == acc_id), None)
                    if not account:
                        print('Error!! Account not found.')
                    else:
                        user.fund_transfer(account)

            except ValueError:
                print('Error!!! Please Enter Valid ID numbers!!')
    elif option ==7:
        new_card = Card()
        new_card.add_values_to_card()
        card_list.append(new_card)
    elif option == 8:
        if not customer_list:
            print("Error!! You must have at least one customer to be able to assign a Card.")
        else:
            print("Enrolled Customers:")
            for user in customer_list:
                user.display_cust_info()
            try:
                cust_id = int(input('Which Customer would you like to assign a Card to?:'))
                user = next((u for u in customer_list if u.cid == cust_id), None)
                if not user:
                    print("Error!! Customer not found.")
                else:
                    print("Available Cards:")
                    for card in card_list :
                        card.display_card_info()

                    card_id = int(input('Which Card is being assigned?:'))
                    card = next((c for c in card_list if c.c_no == card_id), None)
                    if not card:
                        print('Error!! Card not found.')
                    else:
                        user.assign_card(card)
            except ValueError:
                print('Error!!! Please Enter Valid ID numbers!!')
    elif option == 9:
        if not card_list:
            print('Error!! No cards exist yet!!')
        else:
            for card in card_list:
                card.display_card_info()
    elif option == 10:
        f1 = open("Bankdata.dat", "ab")
        pickle.dump(customer_list, f1)
        pickle.dump(card_list, f1)
        f1.close()
        print("Data saved successfully to Bankdata.dat")
    elif option ==11:
        print('Thank you for using the Banking Database, Please come again!')
        break
    else:
        print('Error!!, Please enter a Valid option!!')
        print('=========================================')