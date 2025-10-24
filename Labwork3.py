#define a class Book(Bookid, Bookname, Title, Author)
#define a class user(userID, username, Booksborrowed=[])

#create 5 book object
#creat 2 user objects
#add books to the users
 print('3. Display User information')
 print('4. Checkout Book')
 print('5. Return Book')
 print('------------------------------------------')
 print('Book Options:')
 print('6.Add a new book to the database')
 print("7.Edit a book's information in the database")
 print('8. Display All Books')
 print('-------------------------------------------')
 print('Author Options:')
 print('9.Add an Author to the database')
 print('10.Edit Author information in the database')
 print('11. Display Author information')
 print('--------------------------------------------')
 print('12. Exit')
 print('-------------------------------------------')
try:
option = int(input('Option Selected:'))
except ValueError:
print ('Error! Please input a valid option!')
continue
if option == 1:
new_user = User_class()
new_user.New_user()
user_list.append(new_user)
elif option == 2:
if not user_list:
print('Error!! No Users currently exists!!')
else:
print('Enrolled Users:')
for user in user_list:
user.Display_user()
while True:
try:
User_select = int(input("Which user would you like to Edit? Enter User ID: "))
user_searched = 0
for user in user_list:
if user.user_id == User_select:
user_searched = user

CS 1233 – Object Oriented Programming


break
if user_searched:
user_searched.Edit_user()
print("User info updated")
print('_____________________________________')
break
else:
print('Error!!! User ID not found')
print('_____________________________________')
break
except ValueError:
print("Please enter a valid number.")
elif option ==3:
if not user_list:
print ('Error!! No users exist yet!!')
else:
for user in user_list:
user.Display_user()
elif option ==4:
if not user_list:
print("Error!! You must have at least one user to be able to checkout.")
else:
print("Enrolled Users:")
for user in user_list:
user.Display_user()
try:
user_id = int(input('Which User is checking out a book?:'))
user = next((u for u in user_list if u.user_id == user_id), None)
if not user:
print("Error!! User not found.")
else:
print("Available Books:")
for book in book_list:
book.Display_book()
book_id = int(input('Which Book is being checked out?:'))
book = next((b for b in book_list if b.book_id == book_id), None)
if not book:
print('Error!! Book not found.')
else:

CS 1233 – Object Oriented Programming


user.Bookcheckout(book)
print(f'{user.name} checked out {book.book_title} successfully!')
except ValueError:
print('Error!!! Please Enter Valid ID numbers!!')
elif option ==5:
if not user_list:
print("Error!! You must have at least one user to be able to return a book.")
else:
print("Enrolled Users:")
for u in user_list:
u.Display_user()
try:
user_id = int(input("Which user is returning a book?: "))
user = next((u for u in user_list if u.user_id == user_id), None)
if not user:
print("Error!! User not found.")
elif not user.booksborrowed:
print(f"{user.name} has no borrowed books.")
else:
print("Borrowed Books:")
for b in user.booksborrowed:
print(f"{b.book_id}: {b.book_title}")
book_id = int(input("Which book is being returned?: "))
book = next((b for b in user.booksborrowed if b.book_id == book_id), None)
if not book:
print("Error!! Book not found in borrowed list.")
else:
user.Bookreturn(book)
print(f"{user.name} returned '{book.book_title}' successfully!")
except ValueError:
print("Please enter valid numeric IDs.")
elif option == 6:
new_book = Book_class()
new_book.New_book()
book_list.append(new_book)
elif option == 7:
print('Current Book Index:')
for book in book_list:
book.Display_book()

CS 1233 – Object Oriented Programming


while True:
try:
Book_select = int(input("Which Book information would you like to Edit?
Enter Book ID: "))
Book_searched = 0
for book in book_list:
if book.book_id == Book_select:
Book_searched = book
break
if Book_searched:
Book_searched.Edit_book()
print("Book info updated")
print('_____________________________________')
break
else:
print('Error!!! Book ID not found')
print('_____________________________________')
break
except ValueError:
print("Please enter a valid number.")
elif option ==8:
for book in book_list:
book.Display_book()
elif option == 9:
new_author = Author_class()
new_author.Add_Author()
Author_list.append(new_author)
elif option == 10:
print('Current Author Index:')
for author in Author_list:
author.Display_Author()
try:
author_id = int(input("Which Author's information would you like to Edit? Enter
Author ID: "))
author_searched = next((a for a in Author_list if a.author_id == author_id), None)
if author_searched:
author_searched.Edit_author()
print("Author info updated")

CS 1233 – Object Oriented Programming



print('_____________________________________')
else:
print('Error!!! Author ID not found')
print('_____________________________________')
except ValueError:
print("Please enter a valid number.")
elif option ==11:
for author in Author_list:
author.Display_Author()
elif option ==12:
print('Thank you for using the Library Database, Please come again!')
break
else:
print('Error!!, Please enter a Valid option!!')
print('=========================================')

Paste the screenshots of all possible [all the operation] outputs: (3pts)

CS 1233 –