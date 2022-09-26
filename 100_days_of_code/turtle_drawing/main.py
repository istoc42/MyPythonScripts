from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("deepskyblue")

screen = Screen()
screen.colormode(255)

# Draw a square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

# Draw a dashed line
# for i in range(0, 14):
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)
#     timmy.pd()

# Draw different shapes inside each other
sides = 4
while sides < 21:
    # Get random rgb values
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    # Change pen to random color
    timmy.color(r, g, b)
    timmy.pencolor(r, g, b)
    # Calculate angle of shapes 
    angle = 360 / sides
    for x in range(sides):
        timmy.forward(100)
        timmy.right(angle)
    # Iterate sides
    sides += 1
        
screen.exitonclick()

