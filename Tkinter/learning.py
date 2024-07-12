from tkinter import *
from PIL import Image, ImageTk #take jpg file too otherwise it wont take jpg  file


root = Tk() #basic gui build

root.title("Prayas")

#width height
root.geometry("444x444")

#width height
root.minsize(100,100)
root.maxsize(1200,980)

labell = Label(text="Calculator") # provides text in the gui
labell.pack()

#images
# photo = PhotoImage(file="Tkinter/0-02-03-f7610f22968c5ddfc154f405b908ed0881abfb65468ff9f7e366c43db0ed3938_2210bbb286ba0f6c.png")
# image_label = Label(image=photo)
# image_label.pack()


#for jpg
# image = Image.open("Tkinter/images.jpg")
# photo = ImageTk.PhotoImage(image)

# lavel = Label(image=photo)
# lavel.pack()


text_label = Label(text="Rajesh Hamal born 9 June 1964[1]) is a Nepalese " 
,bg="red",
fg="white",
padx=113,
pady=113,
font=("times new roman",19,"italic"),
borderwidth=4,
relief=SUNKEN)


text_label.pack(side=BOTTOM,anchor="se",fill=X,)  #move text to the left and to the south east side

#gui logic
root.mainloop()  #make interactive



#important label options:
# text - add the Text
# bd = background
# fg = fokreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border style USE TO STYLE IN THE BORDER

#IMPORTANT PACK OPTION:
# ANCHOR = NE sARXA EWNS
# SIDE = TOP BOTTOM LEFT RIGHT
# fill = it helps to make the value constant as if we stretch the window the background color will also stretch / responsive
# padx
# pady
