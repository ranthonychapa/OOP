print("Welcome to our calculation application!")
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit Application")

    option = input("Enter your choice: ")

    if option == "1":
        n1 = int(input("Please Enter the first number: "))
        n2 = int(input("Please Enter the second number:"))
        tot = n1 + n2
        print("The sum of the two numbers is:",tot)

    elif option == "2":
        n1 = int(input("Please Enter the first number: "))
        n2 = int(input("Please Enter the second number:"))
        tot = n1 - n2
        print("The difference of the two numbers is:", tot)
    elif option == "3":
        n1 = int(input("Please Enter the first number: "))
        n2 = int(input("Please Enter the second number:"))
        tot = n1 * n2
        print("The product of the two numbers is:", tot)
    elif option == "4":
        n1 = int(input("Please Enter the first number: "))
        n2 = int(input("Please Enter the second number:"))
        tot = n1 / n2
        print("The quotient of the two numbers is:", tot)
    elif option == "5":
        print("Thank you for using our calculator application, please come again!")
        break
    else:
        print("Error, not a valid option! Please input one of the following options:")

