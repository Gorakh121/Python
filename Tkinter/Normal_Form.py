from tkinter import *


root = Tk()
root.geometry("555x555")

Label(root, text="Name").grid(pady=5,row=0)
Label(root, text="Address").grid(pady=5,row=1)
Label(root, text="Phone-Nb").grid(pady=5,row=2)
Label(root, text="Height").grid(pady=5,row=4)
Label(root, text="Weight").grid(pady=5,row=3)
Label(root, text="Email").grid(pady=5,row=5)
Label(root, text="Gender").grid(pady=5,row=6)

nameValue = StringVar()
addressValue = StringVar()
PhoneValue = IntVar()
HeightValue = IntVar()
WeightValue = IntVar()
EmailValue = StringVar()
GenderValueMale = IntVar()
GenderValueFemale = IntVar()

nameEntry = Entry(root, textvariable=nameValue).grid(column=4, row=0,pady=5)
addressEntry = Entry(root, textvariable=addressValue).grid(column=4, row=1,pady=5)
PhoneEntry = Entry(root, textvariable=PhoneValue).grid(column=4, row=2,pady=5)
HeightEntry = Entry(root, textvariable=HeightValue).grid(column=4, row=3,pady=5)
WeightEntry = Entry(root, textvariable=WeightValue).grid(column=4, row=4,pady=5)
EmailEntry = Entry(root, textvariable=EmailValue).grid(column=4, row=5,pady=5)

Gender_Check = Checkbutton(text="Male" ,variable=GenderValueMale).grid(column=4, row=6, pady=5)
Gender_Check_Female = Checkbutton(text="Female", variable=GenderValueFemale).grid(column=5, row=6, pady=5)

def value():
    with open("data.txt", "w") as f:
        f.write(f"Name: {nameValue.get()}\n")
        f.write(f"Address: {addressValue.get()}\n")
        f.write(f"Phone: {PhoneValue.get()}\n")
        f.write(f"Height: {HeightValue.get()}\n")
        f.write(f"Weight: {WeightValue.get()}\n")
        f.write(f"Email: {EmailValue.get()}\n")
        f.write(f"Gender: {GenderValueMale.get()}\n")
        f.write(f"Gender: {GenderValueFemale.get()}\n")



Button(root, text="Submit",command=value).grid(pady=5)




root.mainloop()