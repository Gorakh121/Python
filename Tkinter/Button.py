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