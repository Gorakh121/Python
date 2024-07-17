from tkinter import *
from PIL import Image, ImageTk  
from tkinter.messagebox import showinfo #for about section/ display the pop up messages
from tkinter.filedialog import askopenfilename, asksaveasfilename  # for open and for save the file
import os  # to get access from operating system

root = Tk()
root.geometry("444x444")
root.title("Notepad")
color1 = '#262726'


def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def newFile():
    global file  # use to open save read write file from os
    root.title("Untilted Notepad")
    file = None
    textarea.delete(1.0,END)  # 1.0 means first line to end of the page delete so it comes with blank space

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
    filetypes=[("all files", "*.*"),
    ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0,f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untilted.txt",
        defaultextension=".txt",
        filetypes=[("all files", "*.*"),
        ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file ,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ "- Notepad")
            print("file save")

    else:
        f = open(file ,"w")
        f.write(textarea.get(1.0,END))
        f.close()


def cutfile():
    textarea.event_generate(("<<Cut>>"))  #todo : its a tkinter default function 


def copyfile():
    textarea.event_generate(("<<Copy>>"))


def pastefile():
    textarea.event_generate(("<<Paste>>"))


def aboutfile():
    showinfo("Notepad", "Notepad by Gorakh")


f1 = Frame(root, bg=rgb_to_hex(45, 45, 44) , borderwidth=4)
f1.pack( fill = X)


#todo: menu bar
Main_menu = Menu(root)

#todo : File menu bar
m1 = Menu(Main_menu, tearoff=0)
m1.add_command(label="New", command=newFile)
m1.add_command(label="Open", command=openfile)
m1.add_command(label="Save ", command=savefile)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
Main_menu.add_cascade(label="File" ,menu=m1)
root.config(menu=Main_menu)

#todo: Edit menu bar
m2 = Menu(Main_menu, tearoff=0)
m2.add_command(label="Cut ", command=cutfile)
m2.add_command(label="Copy", command=copyfile)
m2.add_command(label="Paste ", command=pastefile)
Main_menu.add_cascade(label="Edit" ,menu=m2)
root.config(menu=Main_menu)

#todo: Help menu bar
m3 = Menu(Main_menu, tearoff=0)
m3.add_command(label="About Notepad", command=aboutfile)
Main_menu.add_cascade(label="Help", menu=m3)
root.config(menu=Main_menu)

#todo: text area
textarea =  Text(root, font="lucida 13")
file = None
textarea.pack(fill=BOTH, expand=True)

#todo:scroll bar
Scroll = Scrollbar(textarea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=Scroll.set)

root.mainloop()