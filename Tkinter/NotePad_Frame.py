from tkinter import *

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

color1 = '#262726'

root = Tk()
root.geometry("444x444")
root.title("Notepad")

f1 = Frame(root, bg=rgb_to_hex(45, 45, 44) , borderwidth=4)
f1.pack( fill = X)


button1 = Button(f1 ,
text = "File",
bg = rgb_to_hex(45, 45, 44),
activebackground = rgb_to_hex(45, 45, 44),
activeforeground="white",
fg = "white",
borderwidth=0
)
button1.pack(side=LEFT, pady=2)
button1.pack(padx=2)

button2 = Button(f1 ,
text="Edit",
bg=rgb_to_hex(45, 45, 44),
fg="white",
activebackground = rgb_to_hex(45, 45, 44),
activeforeground="white",
borderwidth=0
)
button2.pack(side=LEFT, pady=2)
button2.pack(padx=15)

button3 = Button(f1 ,
text="View",
bg=rgb_to_hex(45, 45, 44),
fg="white",
activebackground = rgb_to_hex(45, 45, 44),
activeforeground="white",
borderwidth=0
)
button3.pack(side=LEFT, pady=2)
button3.pack(padx=2)

f2 = Frame(root)
f2.pack( fill = X)
f2.pack(fill = Y)

l2 = Label(f2,
bg= color1,
fg="black",
font=("times new roman",10))
l2.pack()

root.mainloop()