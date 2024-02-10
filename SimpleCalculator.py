#Simple calculator, capable of addition

from tkinter import *

calc = Tk()
calc.title('Addition Calulator')

e = Entry(calc, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def press(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def press_clear():
    e.delete(0, END)
    global f_term
    f_term = int(0)

def press_add():
    first_term = e.get()
    global f_term
    f_term = int(first_term)
    e.delete(0, END)

def press_equal():
    second_term = int(e.get())
    e.delete(0, END)
    answer = f_term + second_term
    e.insert(0, answer)

button_1 = Button(calc, text ='1', padx=40, pady=20, command=lambda: press(1))
button_2 = Button(calc, text ='2', padx=40, pady=20, command=lambda: press(2))
button_3 = Button(calc, text ='3', padx=40, pady=20, command=lambda: press(3))
button_4 = Button(calc, text ='4', padx=40, pady=20, command=lambda: press(4))
button_5 = Button(calc, text ='5', padx=40, pady=20, command=lambda: press(5))
button_6 = Button(calc, text ='6', padx=40, pady=20, command=lambda: press(6))
button_7 = Button(calc, text ='7', padx=40, pady=20, command=lambda: press(7))
button_8 = Button(calc, text ='8', padx=40, pady=20, command=lambda: press(8))
button_9 = Button(calc, text ='9', padx=40, pady=20, command=lambda: press(9))
button_0 = Button(calc, text ='0', padx=40, pady=20, command=lambda: press(0))

button_add = Button(calc, text ='+', padx=39, pady=20, command=press_add)
button_equal = Button(calc, text ='=', padx=87, pady=20, command=press_equal)
button_clear = Button(calc, text ='AC', padx=82, pady=20, command=press_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

calc.mainloop()