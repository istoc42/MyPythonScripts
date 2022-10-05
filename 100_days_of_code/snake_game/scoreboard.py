from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Segoe UI', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game\data.txt") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1 
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
      
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # TODO Write to the data.txt file here
            with open("snake_game\data.txt", mode="w") as high_score_file:
                high_score_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()  
         
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)     
