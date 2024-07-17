from tkinter import *

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


root = Tk()
root.geometry("444x444")

frame = Frame(root)
frame.pack(side= LEFT , anchor=NW)

b1 = Button(frame, fg="red", text="prayas",
activebackground = rgb_to_hex(45, 45, 44),  #backgroung color changes when we click 
activeforeground=  rgb_to_hex(45, 45, 44)  # text color changes when we click
)
b1.pack()

root.mainloop()

# button1 = Button(f1 ,
# text = "File",
# bg = rgb_to_hex(45, 45, 44),
# activebackground = rgb_to_hex(45, 45, 44),
# activeforeground="white",
# fg = "white",
# borderwidth=0
# )
# button1.pack(side=LEFT, pady=2)
# button1.pack(padx=2)

# button2 = Button(f1 ,
# text="Edit",
# bg=rgb_to_hex(45, 45, 44),
# fg="white",
# activebackground = rgb_to_hex(45, 45, 44),
# activeforeground="white",
# borderwidth=0
# )
# button2.pack(side=LEFT, pady=2)
# button2.pack(padx=15)

# button3 = Button(f1 ,
# text="View",
# bg=rgb_to_hex(45, 45, 44),
# fg="white",
# activebackground = rgb_to_hex(45, 45, 44),
# activeforeground="white",
# borderwidth=0
# )
# button3.pack(side=LEFT, pady=2)
# button3.pack(padx=2)