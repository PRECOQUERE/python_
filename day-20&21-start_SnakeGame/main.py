# 20~21일차 screen.size 600,600 STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
# √ make snake body
# √ move the snake
# √ control the snake
# -----------------------------
# √ Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

import turtle as t
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
BD_1 = 290
BD_2 = -290
screen = t.Screen()
screen.title("The Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while(game_is_on) :
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Snake eat food
    if snake.head.distance(food) < 15 :
        scoreboard.increase_score()
        snake.extend()
        food.move_position()
    
    # Detect collision with wall
    if snake.head.xcor() > BD_1 or snake.head.xcor() < BD_2 or snake.head.ycor() > BD_1 or snake.head.ycor() < BD_2 :
        scoreboard.reset()
        snake.reset_snake()

    # Detect collsision with tail
    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10 :
            scoreboard.reset()
            snake.reset_snake()
        
screen.exitonclick()