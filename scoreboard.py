from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        
        self.score = 0
        self.color("White")
        self.goto(0,280)
        self.hideturtle()
        
        with open("data.txt") as scoreKeeper:
            self.highScore = int(scoreKeeper.read())

        self.write(arg=f"Score = {self.score} HighScore = {self.highScore}" ,move=False, align="center", font= ('Courier' , 15 , 'normal'))

    #game-over Sequence
    def game_over(self):

        self.clear()
        if self.score > self.highScore:
            self.highScore = self.score
            self.score = 0 

        self.write(arg=f"Score = {self.score} HighScore = {self.highScore}" ,move=False, align="center", font= ('Courier' , 15 , 'normal'))

        with open("data.txt" ,mode="w") as scoreKeeper:
            scoreKeeper.write(str(self.highScore))

    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score = {self.score} HighScore = {self.highScore}" ,move=False, align="center", font= ('Courier' , 15 , 'normal'))
        