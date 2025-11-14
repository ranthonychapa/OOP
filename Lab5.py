import tkinter as tk
from tkinter import *
top = Tk()
top.geometry('500x800')
display = Text(width=35, height=2)
display.place(x= 150,y =40)
display2 = Text(width=34, height=2)
display2.place(x= 150, y = 230)
text_Box = Text(width=35, height=2)
text_Box.place(x= 150,y =325)
text_Box2 = Text(width=34, height=2)
text_Box2.place(x= 150, y = 515)

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
        text_Box2.delete(1.0, END)
        for i in self.element:
            print(i)
            text_Box2.insert(tk.INSERT, f'{i},')
    def push_stack_of_queue(self):
        self.element.append((display2.get(1.0, 'end-1c')))
    def display_Stack_o_Queue(self):
        print('Queue in Stack:')
        text_Box2.delete(1.0, END)
        for i in self.element:
            print(i)
            text_Box2.insert(tk.INSERT, f'[{i}]')

q1 = Queue()
q2 = Queue()
s1= Stack()
s2 =Stack()


B1 = Button(top, text='Enqueue', width=10, height=5, command=lambda: q1.enqueue())
B1.place(x=50, y=15)
B2 = Button(top, text='Dequeue', width=10, height=5, command=lambda: q1.dequeue())
B2.place(x=50, y=110)
B3 = Button(top, text='Display Queue 1', width=10, height=5, command=lambda: q1.displayqueue())
B3.place(x=50, y=205)
####
B2 = Button(top, text='Push', width=10, height=5, command=lambda: s1.push())
B2.place(x=50, y=300)
B3 = Button(top, text='pop', width=10, height=5, command=lambda: s1.pop())
B3.place(x=50, y=395)
B_plus = Button(top, text='Display Stack 1', width=10, height=5, command=lambda: s1.displayStack())
B_plus.place(x=50, y=490)
B_push_Queue = Button(top, text='Push Queue 1', width=10, height=5, command=lambda: s2.push_stack_of_queue())
B_push_Queue.place(x=50, y=585)
B_Display_QS = Button(top, text='Display SoQ', width=10, height=5, command=lambda: s2.display_Stack_o_Queue())
B_Display_QS.place(x=50, y=680)





top.mainloop()