from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I Clicked a Button!!")
    myLabel.pack()

def myClick2():
    
    myLabel = Label(root, text = "Look! I Clicked a Button!!", fg = "white", bg="green")
    myLabel.pack()

    #destroy()で.packが破壊され非表示
    #myLabel.destroy()

    #.pack()使用時は.pack_forget()で非表示
    #myLabel.pack_forget()
    
    #.place使用時は.place_forget()で非表示
    #myLabel.place(x = 10, y = 130)
    #myLabel.place_forget()

#ボタン無効設定
myButton1 = Button(root, text = "Don't Click Me!", state = DISABLED)
myButton1.pack()

#ボタンサイズ(x=横幅、y=縦幅) ※.pack()しないと反映されない command = myClick関数を呼び出して関数内処理をアタッチ(ボタンを押すだけ何度も表示)
myButton2 = Button(root, text = "Click Me!", padx = 50, pady = 30, command = myClick)
myButton2.pack()

#myClick2関数で非表示のサンプル fg="blue"で文字色青色、bg = tkでは現在対応していない
myButton3 = Button(root, text = "Click Me!!", padx = 20, pady = 10, command = myClick2)
myButton3["fg"] = "red"
myButton3["bg"] = "blue"
myButton3.pack()

#myClick関数でイベント、ボタン背景は下記の設定で変数を作り、それに色を割り当てることで赤色にすることができた[2022/12/10現在]
highlightbackground = "color"
myButton4 = Button(text = "Click Me!!", command = myClick, highlightbackground = "red")
myButton4.pack()

root.mainloop()