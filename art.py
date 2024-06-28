
import turtle
import colorsys

wn = turtle.Screen()
wn.setup(768,76)
wn.title("prayas")
wn.bgcolor("black")


#RAdha
b = turtle.Turtle()
b.color('orange')
b.up()
b.speed(0)
b.seth(0)
b.fd(22)
b.seth(90)
b.fd(103)
b.down()
b.circle(50)
wn.mainloop()