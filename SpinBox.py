from tkinter import *

window = Tk()

window.title('Spin box')

window.geometry('350x200')

var = IntVar()
var.set(36)

spin = Spinbox(window, from_=0, to=100, width=10)

spin1 = Spinbox(window, values=(3,8,11), width=10)

spin2 = Spinbox(window, from_=0, to=100, width=10, textvariable=var)

spin.grid(column=0, row=0)
spin1.grid(column=0, row=1)
spin2.grid(column=0, row=2)


window.mainloop()