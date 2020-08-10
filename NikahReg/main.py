from tkinter import *

root = Tk()

mylabe = Label(root, text='Hello world')
mylabe1 = Label(root, text='Hello world 2')
mylabe2 = Label(root, text='Hello world 3')

mylabe.grid(row=0,column=0)
mylabe1.grid(row=1,column=1)
mylabe2.grid(row=2,column=2)

root.mainloop()