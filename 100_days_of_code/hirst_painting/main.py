import random
from turtle import Turtle, Screen

colors = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44)]

### Functions

# Function to return a random color from the list as a tuple
def get_random_color():
    return random.choice(colors)

# Function to draw a row of dots
def draw_row_of_dots(starting_x, starting_y, number_of_dots):
    timmy.penup()
    timmy.goto(starting_x, starting_y)
    
    for x in range(number_of_dots):
        current_color = get_random_color()
        timmy.pencolor(current_color)
        timmy.color(current_color)
        timmy.dot()
        timmy.forward(65)
        
# Screen settings
screen = Screen()
screen.colormode(255)

# Turtle settings
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.pensize(20)

### Turtle commands

# Starting position to bottom left corner
pos_x = -300
pos_y = -300
for i in range(1, 11):
    draw_row_of_dots(pos_x, pos_y, 10)
    # pos_x += 100
    pos_y += 65
    print(f'x = {pos_x}')
    print(f'y = {pos_y}')









screen.exitonclick()