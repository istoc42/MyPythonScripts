from turtle import Screen
from paddle import Paddle
from net import Net
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

net = Net()
l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
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
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect top and bottom wall collision
    if ball.ycor() > 275:
        print("Ball hit the top wall")
        ball.moving_up = False

    if ball.ycor() < -275:
        print("Ball hit the bottom wall") 
        ball.moving_up = True

    # Detect paddle collision
    if ball.distance(r_paddle) < 20:
        print("Ball hit right paddle")
        ball.moving_right = False
        ball.move_speed *= 0.9
        
    if ball.distance(l_paddle) < 20:
        print("Ball hit left paddle")
        ball.moving_right = True   
        ball.move_speed *= 0.9
  
    if ball.xcor() > 350 and ball.distance(r_paddle) < 50:
        print("Ball hit right paddle")
        ball.moving_right = False
    
    if ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        print("Ball hit left paddle")
        ball.moving_right = True

    # Detect paddle miss
    if ball.xcor() > 400:
        scoreboard.increase_l_score()
        ball.ball_refresh()
        ball.moving_right = False
        
    if ball.xcor() < -400:
        scoreboard.increase_r_score()
        ball.ball_refresh()
        ball.moving_right = True
        
    
    

screen.exitonclick()