#No decimal capability

from tkinter import *

calc = Tk()
calc.title('Money Calulator')

e = Entry(calc, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def press(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def press_clear():
    global f_term
    global action
    f_term = float(0)
    action = 'NUL'
    e.delete(0, END)

def press_plumin():
    term = e.get()
    e.delete(0, END)
    e.insert(0, float(term) * -1)

def press_percent():
    term = e.get()
    e.delete(0, END)
    e.insert(0, float(term)/100)

def press_divide():
    global f_term
    global action
    action = 'DIV'
    f_term = float(e.get())
    e.delete(0, END)

def press_mult():
    global f_term
    global action
    action = 'MUL'
    f_term = float(e.get())
    e.delete(0, END)

def press_minus():
    global f_term
    global action
    action = 'MIN'
    f_term = float(e.get())
    e.delete(0, END)

def press_add():
    global f_term
    global action
    action = 'ADD'
    f_term = float(e.get())
    e.delete(0, END)

def press_equal():
    if action == 'ADD':
        answer = str(f_term + float(e.get()))
    elif action == 'MIN':
        answer = str(f_term - float(e.get()))
    elif action == 'MUL':
        answer = str(f_term * float(e.get()))
    elif action == 'DIV':
        answer = str(f_term / float(e.get()))
    e.delete(0, END)
    e.insert(0, answer)

def press_dec():
    current = e.get()
    e.delete(0, END)
    current = str(e.get()) + '.'
    e.insert(0, current)

button_1 = Button(calc, text ='1', padx=45, pady=20, command=lambda: press(1))
button_2 = Button(calc, text ='2', padx=46, pady=20, command=lambda: press(2))
button_3 = Button(calc, text ='3', padx=42, pady=20, command=lambda: press(3))
button_4 = Button(calc, text ='4', padx=45, pady=20, command=lambda: press(4))
button_5 = Button(calc, text ='5', padx=46, pady=20, command=lambda: press(5))
button_6 = Button(calc, text ='6', padx=42, pady=20, command=lambda: press(6))
button_7 = Button(calc, text ='7', padx=45, pady=20, command=lambda: press(7))
button_8 = Button(calc, text ='8', padx=46, pady=20, command=lambda: press(8))
button_9 = Button(calc, text ='9', padx=42, pady=20, command=lambda: press(9))
button_0 = Button(calc, text ='0', padx=98, pady=20, command=lambda: press(0))
button_dec = Button(calc, text ='.', padx=43, pady=20, command=lambda: press_dec)

button_add = Button(calc, text ='+', padx=40, pady=20, command=press_add)
button_minus = Button(calc, text='-', padx=41, pady=20, command=press_minus)
button_divide = Button(calc, text='/', padx=42, pady=20, command=press_divide)
button_mult = Button(calc, text='x', padx=41, pady=20, command=press_mult)
button_equal = Button(calc, text ='=', padx=40, pady=20, command=press_equal)
button_clear = Button(calc, text ='AC', padx=40, pady=20, command=press_clear)
button_plumin = Button(calc, text = '+/-', padx=40, pady=20, command=press_plumin)
button_percent = Button(calc, text = '%', padx=40, pady=20, command=press_percent)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0, columnspan=2)
button_dec.grid(row=5, column=2)

button_clear.grid(row=1, column=0)
button_plumin.grid(row=1, column=1)
button_percent.grid(row=1, column=2)

button_divide.grid(row=1, column=3)
button_mult.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=3)

calc.mainloop()