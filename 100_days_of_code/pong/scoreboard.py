from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Segoe UI', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.write(arg=f"{self.l_score}        {self.r_score}", align=ALIGNMENT, font=FONT)
        
    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(arg=f"{self.l_score}        {self.r_score}", align=ALIGNMENT, font=FONT)
    
    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(arg=f"{self.l_score}        {self.r_score}", align=ALIGNMENT, font=FONT)