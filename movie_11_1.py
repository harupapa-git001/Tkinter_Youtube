#以下コピペで動きます

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap("icon_img.ico")

frame = LabelFrame(root, text="This is my Frame...", labelanchor="nw")


b = Button(frame, text="Don't Click Here!" , command=frame.quit)
b.grid(row=0, column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=1, column=1)


frame.pack(side=TOP)
#frame.grid(row=0,column=0)




frame1 = LabelFrame(root, text="This is my Frame1...", labelanchor="ne")
frame1.propagate(False)
#frame1.grid(row=0,column=1)

b3 = Button(frame1, text="Don't Click Here!" , command=frame.quit)
b3.grid(row=0, column=0)

b4 = Button(frame1, text="...or here!")
b4.grid(row=1, column=1)


frame1.pack(side=BOTTOM)


frame2 = LabelFrame(root, text="This is my Frame2...", labelanchor="sw")
frame2.propagate(False)
#frame1.grid(row=0,column=1)

b5 = Button(frame2, text="Don't Click Here!" , command=frame.quit)
b5.grid(row=0, column=0)

b6 = Button(frame2, text="...or here!")
b6.grid(row=1, column=1)


frame2.pack(side=RIGHT)



frame3 = LabelFrame(root, text="This is my Frame3...", labelanchor="se")
frame3.propagate(False)
#frame1.grid(row=0,column=1)

b7 = Button(frame3, text="Don't Click Here!" , command=frame.quit)
b7.grid(row=0, column=0)

b8 = Button(frame3, text="...or here!")
b8.grid(row=1, column=1)


frame3.pack(side=LEFT)



root.mainloop()

# コピペここまで