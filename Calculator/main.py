from tkinter import *

root = Tk()
root.title("Claculator")
root.iconbitmap("calculator-716-461701.png")

entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



def buttonWork(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(number))


def clearButton():
    entry.delete(0, END)


def buttonAddAction():
    number = entry.get()
    global saa
    saa = 1
    global firstNumber
    firstNumber = int(number)
    entry.delete(0, END)


def buttonSubtractionAction():
    number = entry.get()
    global saa
    saa = 2
    global firstNumber
    firstNumber = int(number)
    entry.delete(0, END)


def buttonMultiplyAction():
    number = entry.get()
    global saa
    saa = 3
    global firstNumber
    firstNumber = int(number)
    entry.delete(0, END)


def buttonDevitionAction():
    number = entry.get()
    global saa
    saa = 4
    global firstNumber
    firstNumber = int(number)
    entry.delete(0, END)


def buttonEqualAction():
    number = entry.get()
    entry.delete(0,END)
    global eq
    if saa == 1:
        entry.insert(0, firstNumber + int(number))
    if saa == 2:
        entry.insert(0, firstNumber - int(number))
    if saa == 3:
        entry.insert(0, firstNumber * int(number))
    if saa == 4:
        entry.insert(0, firstNumber // int(number))



button_0 = Button(root, text='0', padx=30, pady=30, command=lambda: buttonWork(0)).grid(row=4, column=0)
button_1 = Button(root, text='1', padx=30, pady=30, command=lambda: buttonWork(1)).grid(row=1, column=0)
button_2 = Button(root, text='2', padx=30, pady=30, command=lambda: buttonWork(2)).grid(row=1, column=1)
button_3 = Button(root, text='3', padx=30, pady=30, command=lambda: buttonWork(3)).grid(row=1, column=2)
button_4 = Button(root, text='4', padx=30, pady=30, command=lambda: buttonWork(4)).grid(row=2, column=0)
button_5 = Button(root, text='5', padx=30, pady=30, command=lambda: buttonWork(5)).grid(row=2, column=1)
button_6 = Button(root, text='6', padx=30, pady=30, command=lambda: buttonWork(6)).grid(row=2, column=2)
button_7 = Button(root, text='7', padx=30, pady=30, command=lambda: buttonWork(7)).grid(row=3, column=0)
button_8 = Button(root, text='8', padx=30, pady=30, command=lambda: buttonWork(8)).grid(row=3, column=1)
button_9 = Button(root, text='9', padx=30, pady=30, command=lambda: buttonWork(9)).grid(row=3, column=2)

button_eq = Button(root, text='=', padx=30, pady=30, command=buttonEqualAction).grid(row=4, column=2)
button_clear = Button(root, text='Clear', padx=20, pady=27, command=clearButton).grid(row=4, column=1)

button_add = Button(root, text='+', padx=30, pady=30, command=buttonAddAction).grid(row=4, column=3)
button_sub = Button(root, text='-', padx=30, pady=30, command=buttonSubtractionAction).grid(row=3, column=3)
button_mul = Button(root, text='*', padx=30, pady=30, command=buttonMultiplyAction).grid(row=2, column=3)
button_dev = Button(root, text='/', padx=30, pady=30, command=buttonDevitionAction).grid(row=1, column=3)

root.mainloop()
