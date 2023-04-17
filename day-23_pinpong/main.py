import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.driving_car()

    # Detect collision with car
    if car_manager.detect_collision((player.position())) :
        game_is_on = False
        scoreboard.game_over()
                                    
    # Next_stage
    if player.ycor() == FINISH_LINE_Y :
        scoreboard.level_up()
        player.clear_stage()
        car_manager.increase_speed()

screen.exitonclick()