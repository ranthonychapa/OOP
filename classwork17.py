import tkinter as tk
from tkinter import *
top = Tk()
top.geometry('500x500')
display = Text(width=35, height=2)
display.place(x= 150,y =135)
display2 = Text(width=34, height=2)
display2.place(x= 150, y = 325)

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        #valueTxt = text(top............)
        x = display.get(1.0, "end-1c")
        self.element.append(x)
        display.delete(1.0, END)

    def dequeue(self):
        self.element.pop(0)

    def displayqueue(self):
        print('Elements in Queue:')
        display2.delete(1.0, END)
        for i in self.element:
            print(i)
            display2.insert(tk.INSERT, f'{i},')

q1 = Queue()
q2 = Queue()



B1 = Button(top, text='Create Queue', width=10, height=5, command=lambda: Queue())
B1.place(x=50, y=15)
B2 = Button(top, text='Enqueue', width=10, height=5, command=lambda: q1.enqueue())
B2.place(x=50, y=110)
B3 = Button(top, text='Dequeue', width=10, height=5, command=lambda: q1.dequeue())
B3.place(x=50, y=205)
B_plus = Button(top, text='Display', width=10, height=5, command=lambda: q1.displayqueue())
B_plus.place(x=50, y=300)
B_minus = Button(top, text='placeholder', width=10, height=5, command=lambda: Queue())
B_minus.place(x=50, y=395)






top.mainloop()