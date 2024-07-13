from turtle import Turtle 

#pixels to move
MOVE_DISTANCE = 20 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.x = 0 
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for i in range(0 ,3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.setx(self.x)
            snake.color("white")
            self.x = self.x - 20
            self.segments.append(snake)

    #movement logic 
    def move(self):
        for seg_num in range(len(self.segments) - 1 , 0 , -1):
            loc = self.segments[seg_num - 1].pos()
            #print(f"{seg_num} : {loc}")
            self.segments[seg_num].goto(loc)

        self.head.forward(MOVE_DISTANCE)
    
    #snake movement
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    

