from turtle import Turtle
import time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
    
    def ball_refresh(self):
        self.goto(0, 0)
        time.sleep(1)
        
    def move_right(self):
        self.forward(5)
    
    def move_left(self):
        self.backward(5)