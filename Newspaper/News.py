from tkinter import *
from PIL import ImageTk, Image

def every_100(text):
    final = ""
    for i in range(0, len(text)):
        final  += text[i]
        if i%100==0 and i!=0:
            final += "\n"
    return final

root = Tk()
root.geometry("1000x1000")
root.title("Gorakh NewsPaper")

texts = []
photos = []
for i in range(0 , 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png") 
    # todo: resize the image
    image = image.resize((225,200), resample= Image.LANCZOS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width= 800, height = 70)
Label(f0, text="Gorakh Newspaper", font="lucida 33 bold").pack()
f0.pack()

Label(f0, text="July 16 2024 ", font="lucida 13 bold").pack()
f0.pack()

f1 = Frame(root, width = 900, height = 200,pady=14)
Label(f1, text=texts[0], padx=22,pady=22).pack(side=LEFT)
Label(f1, image=photos[0], anchor=E).pack()
f1.pack(anchor=W)

f2 = Frame(root, width = 900, height = 200, padx=22, pady=14 )
Label(f2, text=texts[1], padx=22,pady=22).pack(side=RIGHT)
Label(f2, image=photos[1], anchor=E).pack()
f2.pack(anchor=W)

f3 = Frame(root, width = 900, height = 200,  pady=14)
Label(f3, text=texts[2], padx=22,pady=22).pack(side=LEFT)
Label(f3, image=photos[2], anchor=E,padx=20).pack()
f3.pack(anchor=W)

root.mainloop()