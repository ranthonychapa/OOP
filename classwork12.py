import pickle
class Product:
    def __init__(self):
        self.pid = ''
        self.pname = ''
        self.price = 0.0
        self.description =''
    def get_product_details(self):
        while True:
            try:
                self.pid = int(input("Enter Product ID:"))
                self.pname = input("Enter Product name:")
                self.price = float(input('Enter the Item Price:'))
                self.description = input("Enter Product description")
                break
            except ValueError:
                if not self.pid:
                    print('Error input invalid!! Input a valid Product ID!')
                    continue
                if not self.price:
                    print('Error! Invalid input!! Input a valid Price!')
                    continue
    def display_product_info(self):
        print(self.pid)
        print(self.pname)
        print(self.price)
        print(self.description)

p1 = Product()
p1.get_product_details()
p1.display_product_info()

print('Welcome to our store management system!!')
print('Please select on of the following choices!')

while True:
    print('1. Create a Product')
    print('2. Get Info for the product')
    print('3. Display product info')
    print('4. Write product into a file')
    print('5. Read Product file')
    print('6. ')
    option = input('Enter your selection:')

elif option ==4:
f1 = open('product_inventory.dat', 'ab')
pickle.dump(product_obj, f1)

elif option ==5:
    f2 = open('product_invntory.dat', 'rb')
    while 1:
        try:
            recieved_product = pickle.load(f2)
            recieved_product.display_product_info()
        except EOFError:
            print('There was an Error!!')