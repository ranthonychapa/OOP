#define a class Book(Bookid, Bookname, Title, Author)
#define a class user(userID, username, Booksborrowed=[])

#create 5 book object
#creat 2 user objects
#add books to the users
class User_class:
    def __init__(self):#constructor function
        self.user_id=''
        self.name=''
        self.password=''
        self.address=''
        self.phone = ''
        self.emailid = ''
        self.booksborrowed = []
    def New_user(self):
        self.user_id= input('Enter the User ID:')
        self.name = input('Enter the name:')
        self.password = input('Enter the Password')
        self.address =(input("Enter the Address"))
        self.phone = input('Enter the Phone number')
        self.emailid = input('Enter User email')
    def Edit_user(self):
        self.user_id = input('Enter the updated User ID:')
        self.name = input('Enter the updated name:')
        self.password = input('Enter the updated Password')
        self.address = (input("Enter the updated Address"))
        self.phone = input('Enter the updated Phone number')
        self.emailid = input('Enter updated User email')
    def Bookcheckout(self, cc1):
        self.booksborrowed.append(cc1)
    def Bookreturn(self, cc1):
        self.booksborrowed.remove(cc1)
    def Display_user(self):
        print('User ID:', self.user_id)
        print('Name:',self.name)
        print('Password:',self.password)
        print('Address:',self.address)
        print('Phone number::', self.phone)
        print("Email ID:", self.emailid)
        for x in self.booksborrowed:
            print('Borrowed Books:', x.book_title)
        print('________________________________________________')

class Book_class:
    def __init__(self, x, y, z, a, b):
        self.book_id = x
        self.book_title = y
        self.author_id = z
        self.publisher = a
        self.year_published = b
    def New_book(self):
        self.book_id = input("Enter Book ID:")
        self.book_title = input("Enter Book Title")
        self.author_id = input("Enter the Author ID:") #actaully get from the authorclass
        self.publisher = input("Enter the Publisher")
        self.year_published = input("Enter Year of Publication:")
    def Edit_book(self):
        self.book_id = input("Enter Book ID:")
        self.book_title = input("Enter Book Title")
        self.author_id = input("Enter the Author ID:")  # actaully get from the authorclass
        self.publisher = input("Enter the Publisher")
        self.year_published = input("Enter Year of Publication:")
    def Display_book(self):
        print('Book ID:', self.book_id)
        print('Book Title:',self.book_title)
        print('Author ID:',self.author_id)
        print('Publisher:',self.publisher)
        print('Year Published:', self.year_published)
        print('___________________________________________')


class Author_class:
    def __init__(self, x, y, z, a, b, c):
        self.author_id = x
        self.author_name = y
        self.affiliation = z
        self.country = a
        self.phone = b
        self.emailid = c
    def Add_Author(self):
        self.author_id = input('Enter Author ID:')
        self.author_name = input("Enter Author name")
        self.affiliation = input("Enter Author Affiliation")
        self.country = input("Enter Author's country:")
        self.phone = input("Enter Author's phone number:")
        self.emailid = input("Enter Author's Email ID:")
    def Display_Author(self):
        print('Author ID:', self.author_id)
        print('Author name:',self.author_name)
        print('Author Affiliation:',self.affiliation)
        print("Author's Home country:",self.country)
        print('Phone number:', self.phone)
        print("Email ID:", self.emailid)
        print('____________________________________________________')
#main code
print('Welcome to our Library Database!')
whileTrue:
    print('Choose one of the following options:')
    print('User Options:')
    print('1.Add a User to the database')
    print('2.Edit User information in the database')
    print('3. Display User information')
    print('------------------------------------------')
    print('Book Options:')
    print('1.Add a new book to the database')
    print("2.Edit a book's information in the database")
    print('3. Display All Books')
    print('-------------------------------------------')
    print('Author Options:')
    print('1.Add an Author to the database')
    print('2.Edit Author information in the database')
    print('3. Display Author information')
    print('-------------------------------------------')
    try:
        option = int(input('Option Selected:'))
    except ValueError:
        print ('Error! Please input a valid option!')
    if option == 1:


u1 = User_class()
u2 = User_class()
u3 = User_class()
u1.New_user()
u2.New_user()
u3.New_user()
u1.Display_user()
u2.Display_user()
u3.Display_user()

b1 = Book_class('B01', 'A Game of Thrones', 'TempA01','HarperCollins Voyager', '1996')
b2= Book_class('B02', 'Eragon', 'TempA02', 'Paolini LLC', '2002')
b3 =Book_class('B03', 'The Hobbit', 'TempA03', 'Geroge Allen & Unwin', '1937')

u1.Bookcheckout(b1)
u1.Bookcheckout(b2)
u2.Bookcheckout(b1)
u2.Bookcheckout(b2)
u3.Bookcheckout(b2)

u1.Display_user()
u2.Display_user()
u3.Display_user()
