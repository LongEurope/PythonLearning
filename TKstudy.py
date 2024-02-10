from tkinter import *

window = Tk()

e = Entry(window, width=50)
e.pack()
e.insert(0, 'Enter your name: ')

def click():
    hello = 'Hello ' + e.get()
    words = Label(window, text=hello)
    words.pack()

window.mainloop()