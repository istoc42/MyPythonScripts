from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER.", align="center", font=FONT)