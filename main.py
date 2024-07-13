import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("black")
screen.tracer(0)

game_is_on = True


snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()

#Key Binds to Play W A S D 
screen.onkey(snake.up , "w")
screen.onkey(snake.down , "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right , "d")


while game_is_on == True:
    screen.update() #updates the screen 
    time.sleep(0.1)
    
    snake.move()

    #Detects Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        print("collided")
        snake.extend()

    #Detects Collision with itself
    for segment in snake.segmentKeeper[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    #Detects Collision with Wall 
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()