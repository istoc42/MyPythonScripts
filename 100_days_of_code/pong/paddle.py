from turtle import Turtle

LEFT_PADDLE_X = -380
LEFT_PADDLE_Y = 0
RIGHT_PADDLE_X = 380
RIGHT_PADDLE_Y = 0

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=5, stretch_wid=1, outline=5)
        self.penup()
        self.setheading(270)
        paddle_start = starting_position.lower()
        if paddle_start == "left":
            paddle_x = LEFT_PADDLE_X
            paddle_y = LEFT_PADDLE_Y
        elif paddle_start == "right":
            paddle_x = RIGHT_PADDLE_X
            paddle_y = RIGHT_PADDLE_Y
        self.goto(paddle_x, paddle_y)
        
    def move_paddle_up(self):
        self.backward(20)
    
    def move_paddle_down(self):
        self.forward(20)