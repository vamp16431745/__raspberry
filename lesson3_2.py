import tkinter as tk #把套件tkinter改暱稱為tk

class Window(tk.Tk):
    def __init__(self):      #def 相當於建構子
        super().__init__()   #self相當於 this  在python預設可以被省略
        self.title("嘿嘿嘿 我被創建了")
        self.geometry('380X400')
        self.resizable(False,False)

if __name__=="__main__":
    window=Window()
    window.mainloop()