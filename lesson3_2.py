import tkinter as tk #把套件tkinter改暱稱為tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):      #def 相當於建構子
        super().__init__()   #self相當於 this  在python預設可以被省略
        self.title('嘿嘿嘿 我被創建了')
        self.resizable(False, False)
        s = ttk.Style()
        print(s.theme_names())
        print(s.theme_use())
        s.theme_use('classic')
        s.configure('TLabel',foreground='red',background='blue')
        title_label = ttk.Label(self,text="LED控制器",font=('Helvetica', '16'))
        print(title_label.winfo_class())
        title_label.pack(pady=25,padx=100)

        led_btn = ttk.Button(self,text="LED 開")
        led_btn.pack(pady=(10,50))
        
        

if __name__ == "__main__":
    window = Window()
    window.mainloop()