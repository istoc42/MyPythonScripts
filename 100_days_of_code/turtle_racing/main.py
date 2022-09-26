from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Place your bets!", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtles = []
turtle_y = 150

for turtle_index in  range(0, 6):
    current_color = colors[turtle_index]
    turtle_name = f"{current_color}_t"
    turtle_name = Turtle()
    turtle_name.color(current_color)
    turtle_name.shape("turtle")
    turtle_name.penup()
    turtle_name.goto(-225, turtle_y)
    turtle_y -= 50
    all_turtles.append(turtle_name)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            break
        # TODO End loop once a turtle wins.
        
        # TODO Check if user_input matches the winner
        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        

screen.exitonclick()