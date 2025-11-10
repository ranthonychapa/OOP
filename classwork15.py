#calculator
import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x500")

answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(x):
    try:
        if x == '=':
            final_answer = eval(answer.get(1.0, 'end-1c'))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == 'C':
            answer.delete(1.0, END)
        elif x == 'Backspace':
            current = answer.get(1.0, 'end-1c')
            answer.delete(1.0, END)
            answer.insert(1.0, current[:-1])
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)
        answer.insert(tk.INSERT, 'Invalid Expression!!')

B1 = Button(top, text='1', width=10, height=5, command=lambda: show('1'))
B1.place(x=100, y=150)
B2 = Button(top, text='2', width=10, height=5, command=lambda: show('2'))
B2.place(x=200, y=150)
B3 = Button(top, text='3', width=10, height=5, command=lambda: show('3'))
B3.place(x=300, y=150)
B_plus = Button(top, text='+', width=10, height=5, command=lambda: show('+'))
B_plus.place(x=400, y=50)
B_minus = Button(top, text='-', width=10, height=5, command=lambda: show('-'))
B_minus.place(x=400, y=150)
B4 = Button(top, text='4', width=10, height=5, command=lambda: show('4'))
B4.place(x=100, y=250)
B5 = Button(top, text='5', width=10, height=5, command=lambda: show('5'))
B5.place(x=200, y=250)
B6 = Button(top, text='6', width=10, height=5, command=lambda: show('6'))
B6.place(x=300, y=250)
B_multiply = Button(top, text='*', width=10, height=5, command=lambda: show('*'))
B_multiply.place(x=400, y=250)
B7 = Button(top, text='7', width=10, height=5, command=lambda: show('7'))
B7.place(x=100, y=350)
B8 = Button(top, text='8', width=10, height=5, command=lambda: show('8'))
B8.place(x=200, y=350)
B9 = Button(top, text='9', width=10, height=5, command=lambda: show('9'))
B9.place(x=300, y=350)
B_divide = Button(top, text='/', width=10, height=5, command=lambda: show('/'))
B_divide.place(x=400, y=350)
B0 = Button(top, text='0', width=10, height=5, command=lambda: show('0'))
B0.place(x=200, y=450)
B_equals = Button(top, text='=', width=10, height=5, command=lambda: show('='))
B_equals.place(x=400, y=450)
B_Clear = Button(top, text='C', width=10, height=5, command=lambda: show('C'))
B_Clear.place(x=5, y=150)
B_Backspace = Button(top, text='Backspace', width=10, height=5, command=lambda: show('Backspace'))
B_Backspace.place(x=5, y=250)
top.mainloop()
