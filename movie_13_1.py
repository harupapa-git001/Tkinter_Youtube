import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw() # rootウィンドウを表示せずにメッセージボックスだけ表示

# メッセージボックス (情報)
messagebox.showinfo(title="TITLE", message="MESSAGE", detail="DETAIL")
# メッセージボックス (警告)
messagebox.showwarning("TITLE", "MESSAGE", detail="DETAIL")
# メッセージボックス (エラー)
messagebox.showerror("TITLE", "MESSAGE", detail="DETAIL")

# メッセージボックス (はい /いいえ) 
rsp = messagebox.askquestion("TITLE", "MESSAGE", detail="DETAIL")
print(rsp)
# メッセージボックス (OK / キャンセル) 
rsp = messagebox.askokcancel("TITLE", "MESSAGE", detail="DETAIL")
print(rsp)
# メッセージボックス (はい / いいえ) 
rsp = messagebox.askyesno("TITLE", "MESSAGE", detail="DETAIL")
print(rsp)
# メッセージボックス (はい / いいえ / キャンセル)
rsp = messagebox.askyesnocancel("TITLE", "MESSAGE", detail="DETAIL")
print(rsp)
# メッセージボックス (再試行 / キャンセル) 
rsp = messagebox.askretrycancel("TITLE", "MESSAGE", detail="DETAIL")
print(rsp)