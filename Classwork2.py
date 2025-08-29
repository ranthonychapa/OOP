a= int(input("Enter the value of a:"))
b= int(input("Enter the value of b:"))

if a>b:
    print('A is greater')
elif b>a:
    print('B is greater')
else:
    print("They are equal")

c=int(input("Enter the value of c:"))
if a> b and a>c:
    print("A is the greatest")
elif b> a and b>c:
    print("B is the greatest")
else:
    print("C is the greatest")