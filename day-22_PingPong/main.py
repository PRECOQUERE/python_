# √1. make screen
# √2. make l_paddle and move l_paddle
# √3. make r_paddle and move r_paddle
# 4. make ball and move ball
#     - Detect collision with wall
#     - Detect collision with paddle
#     - Detect when paddle misses
# 5. make scoreboard 

from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.title("PingPong Game")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

game_is_on = True
while game_is_on :
    time.sleep(ball.speed)
    screen.update()

    ball.moving()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() == 330 or ball.distance(l_paddle) < 50 and ball.xcor() == -330:
        ball.bounce_x()
    
    # Detect when paddle misses
    if ball.xcor() > 380 :
        scoreboard.plus_s1()
        ball.reset_ball()
    elif ball.xcor() < -380 :
        scoreboard.plus_s2()
        ball.reset_ball()

screen.exitonclick()
