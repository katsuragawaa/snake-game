from scoreboard import Scoreboard
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Game screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for input
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # Detect colision with food
    if snake.head.distance(food) < 15 :
        food.reflesh()
        scoreboard.score_increase()
        snake.extend()

    # Detect colision with edge
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.game_over()
        game_on = False

    # Detect colision with snake
    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10 :
            scoreboard.game_over()
            game_on = False


screen.exitonclick()

