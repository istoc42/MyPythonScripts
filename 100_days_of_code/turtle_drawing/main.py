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

def random_color():
    # Get random rgb values
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    # Change pen and turtle to random color
    timmy.color(r, g, b)
    timmy.pencolor(r, g, b)

# Draw different shapes inside each other
# sides = 4
# while sides < 10:
#     random_color()    
#     # Calculate angle of shapes 
#     angle = 360 / sides
#     for x in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#     # Iterate sides
#     sides += 1

# Draw a random walk
#  Speed up the turtle
# timmy.speed(0)
# # Increase line thickness
# timmy.pensize(15)
# # Generate random walk with same forward distance but random directions
# directions = [0, 90, 180, 270]
# i = 0
# while i <= 100:
#     random_color()
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     i += 1

# Make a spirograph
timmy.speed("fastest")

x = 0
while x <= 360:
    random_color()
    timmy.circle(100)
    x += 5
    timmy.setheading(x)

screen.exitonclick()

