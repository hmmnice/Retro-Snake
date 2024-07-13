from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("White")
        self.goto(0,280)
        self.write(arg=f"Score = {self.score}" ,move=False, align="center", font= ('Courier' , 15 , 'normal'))
        self.hideturtle()
    
    #game-over Sequence
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over" ,move=False, align="center", font= ('Courier' , 30 , 'normal'))
    
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score = {self.score}" ,move=False, align="center", font= ('Courier' , 15 , 'normal'))
        