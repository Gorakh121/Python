from tkinter import *

root = Tk()
root.geometry("444x444")

def myfunc():
    print("Hello world")


# # todo : use to create non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Edit", command=quit)
# root.config(menu=mymenu)

yourmenu = Menu(root)
m1 = Menu(yourmenu, tearoff=0) # todo remove the unwanted menu tearoff
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Open", command=myfunc)
m1.add_separator()  #todo:  underline in the menubar
m1.add_command(label="New Project", command=myfunc)
yourmenu.add_cascade(label="File", menu=m1)
root.config(menu=yourmenu)

root.mainloop()