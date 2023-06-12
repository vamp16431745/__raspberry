import tkinter as tk #把套件tkinter改暱稱為tk

class Window(tk.Tk):
    def __init__(self):      #def 相當於建構子
        super().__init__()   #self相當於 this  在python預設可以被省略
        self.title('嘿嘿嘿 我被創建了')
        self.resizable(False, False)
        title_label = tk.Label(self,text="LED控制器",font=('Helvetica', '16') )
        title_label.pack(pady=25,padx=100)

        led_btn = tk.Button(self,text="LED 開",font=('Helvetica', '16'),padx=20,pady=20)
        led_btn.pack(pady=(10,50))
        

if __name__ == "__main__":
    window = Window()
    window.mainloop()