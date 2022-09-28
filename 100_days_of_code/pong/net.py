from turtle import Turtle

class Net(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 390)
        self.pencolor("white")
        self.right(90)
        for x in range(0, 20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        