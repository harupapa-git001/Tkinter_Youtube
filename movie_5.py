from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_Click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_Add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_Subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtracction"
    f_num = int(first_number)
    e.delete(0, END)

def button_Multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_Divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_Equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))   
    if math == "dot":
        e.insert(0, float(f_num) + int(second_number)) 
def button_Dot():
    first_number = e.get()
    second_number = e.get()
    global f_num
    global math
    math = "dot"
    f_num = float(0)
    e.delete(0, END)
    e.delete(0, -1)
    e.insert(0, str(float(f_num) + float(second_number)))


def button_Clear():
    e.delete(0, END)

#DefineButtons

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_Click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_Click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_Click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_Click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_Click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_Click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_Click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_Click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_Click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_Click(0))

button_add = Button(root, text = "+", padx = 19, pady = 15, command = button_Add)
button_subtract = Button(root, text = "-", padx = 19, pady = 15, command = button_Subtract)
button_multiply = Button(root, text = "x", padx = 19, pady = 15, command = button_Multiply)
button_divide = Button(root, text = "/", padx = 19, pady = 15, command = button_Divide)
button_equal = Button(root, text = "=", padx = 16, pady = 15, command = button_Equal)
button_dot = Button(root, text = ".", padx = 25, pady = 15, command = button_Dot)
button_clear = Button(root, text = "C", padx = 25, pady = 15, command = button_Clear)

#Put the buttons on the screen

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_dot.grid(row = 4, column = 1)
button_clear.grid(row = 4, column = 2)
button_add.grid(row = 0, column = 3)
button_subtract.grid(row = 1, column = 3)
button_multiply.grid(row = 2, column = 3)
button_divide.grid(row = 3, column = 3)
button_equal.grid(row = 4, column = 3)

root.mainloop()