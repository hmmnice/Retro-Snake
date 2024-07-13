from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5 , stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    #Moves the food to a random position on the screen 
    def refresh(self):
        randomCoord = random.randint(-280 , 280)
        self.goto(randomCoord , randomCoord) 