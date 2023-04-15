# √1. create Screen
# √2. create my Paddle & move my Paddle
# √3. create another Paddle & move Paddle
# 4. create Ball & move Ball
#     √ detect collision with wall and bounce
#     √ detect with paddle
#     - detect when paddle misses
# 5. create Scoreboard

from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title("PONG")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
speed = 0.1
while game_is_on :
    if ball.move_speed < 0 : 
        ball.move_speed = 0
        
    time.sleep(ball.move_speed)
    screen.update()
    ball.moving()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.move_speed -= 0.01
    
    # Detect when paddle misses
    if ball.xcor() > 380 :
        ball.reset_pos()
        scoreboard.l_point()
        
    elif ball.xcor() < -380 :
        ball.reset_pos()
        scoreboard.r_point()
    
screen.exitonclick()
