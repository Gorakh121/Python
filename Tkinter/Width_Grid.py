from tkinter import *

root = Tk()
root.geometry("444x444")

username = Label(root, text="Username")
password = Label(root, text="Password")
username.grid()   #default row = 0
password.grid(row=1)  #row changes


#varialble classes in tkinter
# BooleanVar , DoubleVar, IntVar, StringVar


usernameValue = StringVar()
passwordValue = StringVar()

userentry = Entry(root , textvariable=usernameValue)
passwordentry = Entry(root , textvariable=passwordValue)

userentry.grid(row=0, column=1)
passwordentry.grid(row=1, column=1)

def value():
    print("Username:",usernameValue.get())
    print("Password", passwordValue.get())

Button(text="Submit", command=value).grid(column=1)

root.mainloop()