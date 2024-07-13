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
        self.segmentKeeper = []
        self.create()
        self.head = self.segmentKeeper[0]

    def create(self):
        for i in range(0 ,3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.setx(self.x)
            segment.color("white")
            self.x = self.x - 20
            self.segmentKeeper.append(segment)

    #Code can be improved but works for now 

    def extend(self):
        segment = Turtle(shape="square")
        segment.penup()
        segment.setx(self.x)
        segment.color("white")
        segment.goto(self.segmentKeeper[-1].position())
        self.segmentKeeper.append(segment)
        
        
    #movement logic 
    def move(self):
        for seg_num in range(len(self.segmentKeeper) - 1 , 0 , -1):
            loc = self.segmentKeeper[seg_num - 1].pos()
            #print(f"{seg_num} : {loc}")
            self.segmentKeeper[seg_num].goto(loc)

        self.head.forward(MOVE_DISTANCE)
    
    #snake movement with KEYBIND
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
    

