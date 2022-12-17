from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap("icon_img.ico")
#root.withdraw()

# showinfo showwarning showerror askquestion askokcancel askyesno から選ぶ movie_13_1.pyにサンプル

def popup():
    response = messagebox.showinfo(title="This is my Popup!", message="Hello World!", detail="詳細")
    Label(root, text=response).pack()

    response1 = messagebox.askyesno(title="This is my Popup!", message="Hello World!", detail="詳細")
    Label(root, text=response1).pack()

    if response1 == 1:
        Label(root, text="you clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()

    btn = Button(root, text="Exit", command=root.quit)
    btn.pack()
    print(btn)

Button(root, text="Popup", command=popup).pack()


root.mainloop()