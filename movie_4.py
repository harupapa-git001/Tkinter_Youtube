from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()


#ボタン無効設定
myButton1 = Button(root, text = "Enter Your Name!", command = myClick)
myButton1.pack()

root.mainloop()