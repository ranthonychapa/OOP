def area_rectangle():
    L = int(input("Enter the Length of the Rectangle"))
    B = int(input("Enter the Breadth of the Rectangle"))
    print("The Area is:", L*B)

def volume_of_the_cube():
    L = int(input('Enter the Length'))
    B = int(input('Enter the Breadth'))
    W = int(input('Enter the Width'))
    print('The Volume of the cube is:', L*B*W)

def areacirc():
    R = int(input('Please enter the radius:'))
    print('The Area of the circle is:', R*R*3.14)

def circumcirc():
    R = int(input('Please enter the radius:'))
    print('The Circumference of the circle is:', 2*3.14*R)

def spherevol():
    R = int(input('Please enter the radius:'))
    print ('The volume of the sphere is:', 4/3*3.14*R*R*R)
#Main code
print('Welcome to our area and volume calculator!')
while 1:
    print('1.Are of a rectangle')
    print('2. Volume of  a cube')
    print('3. Area of a circle')
    print('4. Circumference of a circle')
    print('5. volume of a sphere')
    print('6. Quit')
    try:
        option = int(input('Please select one of the following options:'))
    except ValueError:
        print('Error, please try a valid option!')
        continue
    if option ==1:
        area_rectangle()
    elif option ==2:
        volume_of_the_cube()
    elif option ==3:
        areacirc()
    elif option ==4:
        circumcirc()
    elif option ==5:
        spherevol()
    elif option==6:
        print('Thank you for using our application!')
        break
    else:
        print('Error, please enter a valid option')

