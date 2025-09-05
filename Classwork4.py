for num in range(1,20):
    if num%2 ==0: #divisible by 2
        print("Even")
    else:
        print ("Odd")
m = int(input("Enter the largest number in the range"))
for num in range (1,m+1):
    n2 = 3 *num
    print (n2)

p = 10000
n = 12 #months
R = 0.02

r = R/(12*100)

EMI = p * r * ((1+r)**n)/((1+r)**n-1)
for time in range (1,n+1):
    balance = p-EMI
    print ("EMI:", EMI)
    print ("Balance:", balance)
    print ("___________________________________________________________________")
    p= balance
    EMI = p * r * ((1 + r) ** n) / ((1 + r) ** n - 1)