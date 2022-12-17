from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap("icon_img.ico")

frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=100, pady=100)
frame.grid(row=0,column=0)

b = Button(frame, text="Don't Click Here!" , command=frame.quit)
b.grid(row=0, column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=1, column=1)

root.mainloop()