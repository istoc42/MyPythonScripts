from turtle import Turtle
import time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.moving_right = True
        self.moving_up = True
        self.move_speed = 0.05
    
    def ball_refresh(self):
        self.goto(0, 0)
        time.sleep(1)
        self.move_speed = 0.1
        
    def move(self):
        if self.moving_right == True:
            new_x = self.xcor() + 10
        else:
            new_x = self.xcor() - 10

        if self.moving_up == True:
            new_y = self.ycor() + 10
        else:
            new_y = self.ycor() - 10
       
        self.goto(new_x, new_y)

    def move_right(self):
        self.setheading(0)
    
    def move_left(self):
        self.setheading(180)