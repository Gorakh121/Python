from tkinter import *

root = Tk()
root.geometry("444x444")
f1 = Frame(root, bg="red", borderwidth=6 , relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="blue", borderwidth=8, relief=SUNKEN)
f2.pack(fill=X)


l1 = Label(f1,text="prays - text editor")
l1.pack( pady=142 )

l2 = Label(f2,text="Welcome to Pras world" , font=("times new roman",19,"italic"))
l2.pack(side=TOP   )




root.mainloop()