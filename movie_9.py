from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap("icon_img.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/icon_img.png")) # .pyからみたファイルの階層とターミナルやコマンドプロンプトのカレントディレクトリに注意
my_img2 = ImageTk.PhotoImage(Image.open("images/img_1.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img_2.png"))

image_list = [my_img1, my_img2, my_img3]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)
#my_label.pack()

def next(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    button_next = Button(root, text=">>", command=lambda: next(image_number+1))
    button_next.grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    button_back.grid(row=1, column=0)

    if image_number == 3:
        button_next["state"] = "disable"

    my_label.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    button_next = Button(root, text=">>", command=lambda: next(image_number+1))
    button_next.grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    button_back.grid(row=1, column=0)

    if image_number == 1:
        button_back["state"] = "disable"

    my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_back.grid(row=1, column=0)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)
button_next = Button(root, text=">>", command=lambda: next(2))
button_next.grid(row=1, column=2)
#button_quit.pack()


root.mainloop()