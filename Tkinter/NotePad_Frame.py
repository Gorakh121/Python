from tkinter import *

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

root = Tk()
root.geometry("444x444")
root.title("Notepad")

f1 = Frame(root, bg=rgb_to_hex(45, 45, 44) , borderwidth=4)
f1.pack( fill = X)

l1 = Label(f1, text="File   Edit   View",
bg = rgb_to_hex(45, 45, 44),
fg = "white",
font = ("times new roman",13))
l1.pack(side=LEFT)

f2 = Frame(root, bg="white")
f2.pack( fill = X)
f2.pack(fill = Y)

l2 = Label(f2,\
bg="white",
fg="black",
font=("times new roman",10))
l2.pack()



root.mainloop()