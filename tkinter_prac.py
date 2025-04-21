from tkinter import*
import random

import pyperclip

win = Tk()
# 標題
win.title("welcome")
# 設視窗大小
win.geometry("809x500+600+600")#寬*高 + x + y
#設定視窗最大最小
win.minsize(width=809, height=500)
win.maxsize(width=809, height=500)

#icons
win.iconbitmap("")#ico檔位置
#function
def sayhi():
    print("hello")
def ok():
    t = en.get()
    lb.config(text = t)

#背景顏色
win.config()
#透明度
# win.attributes("-alpha", 0.4)
#至頂
# win.attributes("-topmost", True)



#label
lb = Label(text = "hello world", bg = "green")
lb.config(text = "change")
lb.pack()

#entry
en = Entry()
en.pack()


#button
btn = Button(text = "click me", bg = "red")
btn.config(width=8, height=4)
btn.config(command= ok)#按鈕備案下十執行sayhi
btn.pack()





win.mainloop()