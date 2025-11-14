import tkinter as tk
from tkinter import *
top = Tk()
top.geometry('500x500')
text_Box = Text(width=35, height=2)
text_Box.place(x= 150,y =135)
display2 = Text(width=34, height=2)
display2.place(x= 150, y = 325)

class Stack:
    def __init__(self):
        self.element = []
    def push(self):
        self.element.append((text_Box.get(1.0, 'end-1c')))
        text_Box.delete(1.0, END)
    def pop(self):
        self.element.pop()
    def displayStack(self):
        print('Element in stack:')
        display2.delete(1.0, END)
        for i in self.element:
            print(i)
            display2.insert(tk.INSERT, f'{i},')

s1= Stack()
s2 =Stack()


B2 = Button(top, text='Push', width=10, height=5, command=lambda: s1.push())
B2.place(x=50, y=110)
B3 = Button(top, text='pop', width=10, height=5, command=lambda: s1.pop())
B3.place(x=50, y=205)
B_plus = Button(top, text='Display Stack', width=10, height=5, command=lambda: s1.displayStack())
B_plus.place(x=50, y=300)







top.mainloop()

s1.push()
s1.pop()
s1.displayStack()