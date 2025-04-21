import tkinter as tk
root = tk.Tk()

root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
# root.iconbitmap('heart_green.ico')
text=tk.Label(root, text='I am Label',
              font="Times 25 bold",
              wraplength=40,
              justify="right") #文字靠右

text.pack() 
 

root.mainloop()