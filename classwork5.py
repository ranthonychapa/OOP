myList = [2,4,8,54, "Justus"]
print(myList)
myList.append(92)
print(myList)
myList.remove(54)
print(myList)
myList.pop()

print(myList)

myList2 = ["Red", "Green", "Blue"]
print(myList2)
myList2[1] = "Orange"
print(myList2)
myList2[2] = "Purple"
print(myList2)

#pratice problem 1

myList3 = []
print("Welcome to our List simulation")
while True:

    print("1. Add an element to the list")
    print('2. Remove a specific element from the list')
    print('3. Pop the last element')
    print('4. Display the list')
    print('5. Sort the Elements in the list')
    print('6. Reverse the Elements in the list')
    print('7. Quit')
    option = int(input("Enter your Choice:"))
    if option == 1:
        print('What would you like to add to the list')
        myList3.append(input())
    elif option == 2:
        print("Which element would you like to remove?")
        myList3.remove(myList3[int(input())])
    elif option == 3:
        myList3.pop()
    elif option ==4:
        print(myList3)
    elif option ==5:
        myList3.sort()
    elif option ==6:
        myList3.reverse()
    elif option == 7:
        print('Thank you for using our list simulation')
        break
    else:
        print('Error invalid input please try again!')

for i in range(len(myList)):
    print(myList[i])

