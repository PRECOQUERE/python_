# 20일차 screen.size 600,600 STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
# 1. make snake body
# 2. move the snake
# 3. control the snake
# -----------------------------
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail
 
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        snake.extend()
        food.refresh()
        sb.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        snake.reset_snake()
        sb.reset_game()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset_snake()
            sb.reset_game()

screen.exitonclick()