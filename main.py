import time
from turtle import Screen
from snake import Snake


screen = Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True

snake = Snake()
screen.listen()

screen.onkey(snake.up , "w")
screen.onkey(snake.down , "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right , "d")


while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


screen.exitonclick()