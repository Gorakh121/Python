from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("444x444")
root.title("Notepad")

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def new():
    print("hello its me Gorakh")

color1 = '#262726'


f1 = Frame(root, bg=rgb_to_hex(45, 45, 44) , borderwidth=4)
f1.pack( fill = X)


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

#todo: menu bar
Main_menu = Menu(root)

#todo : File menu bar
m1 = Menu(Main_menu, tearoff=0)
m1.add_command(label="New tab", command=new)
m1.add_command(label="New window", command=new)
m1.add_command(label="Open", command=new)
m1.add_command(label="Save ", command=new)
m1.add_command(label="Save as ", command=new)
m1.add_command(label="Save all ", command=new)
m1.add_separator()
m1.add_command(label="Page setup ", command=new)
m1.add_command(label="Print ", command=new)
m1.add_separator()
m1.add_command(label="Close tab ", command=new)
m1.add_command(label="Close window ", command=new)
m1.add_command(label="Exit", command=quit)
Main_menu.add_cascade(label="File" ,menu=m1)
root.config(menu=Main_menu)

#todo: Edit menu bar
m2 = Menu(Main_menu, tearoff=0)
m2.add_command(label="Undo", command=new)
m2.add_separator()
m2.add_command(label="Cut ", command=new)
m2.add_command(label="Copy", command=new)
m2.add_command(label="Paste ", command=new)
m2.add_command(label="Delete  ", command=new)
m2.add_separator()
m2.add_command(label="Define with bing  ", command=new)
m2.add_separator()
m2.add_command(label="Find  ", command=new)
m2.add_command(label="Find next ", command=new)
m2.add_separator()
m2.add_command(label="Find previous ", command=new)
m2.add_command(label="Replace  ", command=new)
m2.add_command(label="Go to", command=new)
m2.add_separator()
m2.add_command(label="Select all  ", command=new)
m2.add_command(label="Time/date  ", command=new)
m2.add_separator()
m2.add_command(label="Font  ", command=new)
Main_menu.add_cascade(label="Edit" ,menu=m2)
root.config(menu=Main_menu)

#todo: View menu bar
m3 = Menu(Main_menu, tearoff=0)
m3.add_command(label="Zoom", command=new)
m3.add_command(label="Status bar", command=new)
m3.add_command(label="Word wrap", command=new)
Main_menu.add_cascade(label="view", menu=m3)
root.config(menu=Main_menu)

Text(root, font="lucida 13").pack(fill=BOTH)

root.mainloop()