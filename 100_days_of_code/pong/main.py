from turtle import Turtle, Screen
from paddle import Paddle
from net import Net
from ball import Ball
from scoreboard import Scoreboard
import time

### TO-DO list ###
# Create the Screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
    # TODO Make ball move randomly
# TODO Detect collison with wall and bounce
# TODO Detect collision with paddle
# Detect when paddle misses
# Keep score

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight=300, canvwidth=300)
screen.tracer(0)

net = Net()
l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

# Event listeners
screen.listen()
screen.onkeypress(l_paddle.move_paddle_up, "w")
screen.onkeypress(l_paddle.move_paddle_down, "s")
screen.onkeypress(r_paddle.move_paddle_up, "Up")
screen.onkeypress(r_paddle.move_paddle_down, "Down")

# Main game loop
game_on = True
last_point_to_left = True
while game_on:
    screen.update()
    time.sleep(0.001)
    
    # Choose which direction ball moves at start of round
    if last_point_to_left:
        ball.move_right()
    else:
        ball.move_left()
    
    # Detect paddle collision
    if ball.distance(r_paddle) < 40:
        ball.setheading(180)
        
    if ball.distance(l_paddle) < 40:
        ball.setheading(0)
        
    # Detect paddle miss
    if ball.xcor() > 400:
        scoreboard.increase_l_score()
        ball.ball_refresh()
        last_point_to_left = True
        
    if ball.xcor() < -400:
        scoreboard.increase_r_score()
        ball.ball_refresh()
        last_point_to_left = False
        
    
    

screen.exitonclick()