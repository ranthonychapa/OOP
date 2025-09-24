#queue - fifo
#stack -
myQueue = []
myStack = []

def Enqueue():
    myQueue.append(input('Please enter the name you wish to add to the queue'))


def Dequeue():
    myQueue.remove(myQueue[0])


def Display():
    print(myQueue)

def Enstack():
    myStack1.append(input('Please enter the name you wish to add to the stack'))
def Unstack():
    myStack.pop()
def DispStack():
    print(myStack)

print('Welcome to our queue simulation')
while 1:
    print('1. Add to queue')
    print('2. Remove from queue')
    print('3. Display the queue')
    print('4. Add to stack')
    print('5. Remove from stack')
    print('6. Display the stack')
    print('7. quit')
    try:
        option= int(input('Please enter your choice:'))
    except ValueError:
        print ('Error, Not a valid option!')
        continue
    if option ==1:
        Enqueue()
    elif option ==2:
        Dequeue()
    elif option ==3:
        Display()
    elif option ==4:
        Enstack()
    elif option ==5:
        Unstack()
    elif option ==6:
        DispStack()
    elif option ==7:
        break
    else:
        print("Error, not a valid option!")




