from turtle import *

bgcolor("white")
color("red")
begin_fill()
pensize(3)

# Turn left 50 degrees
left(50)

# Move forward 133 units
forward(133)

# Draw a semi-circle with radius 50 and angle 200
circle(50, 200)

# Turn right 140 degrees
right(140)

# Draw another semi-circle
circle(50, 200)

# Move forward 133 units
forward(133)

end_fill()


penup()  # Lift the pen to move without drawing
goto(-30, 90)  # Move to the desired position
pendown()  # Put the pen down to start drawing text

color("black")  # Set text color
write("WHO?", font=("Arial", 12, ))


done()
