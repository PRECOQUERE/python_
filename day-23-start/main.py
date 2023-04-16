# √1. 거북이는 위로만 움직임
# 2. y축 범위에 자동차 무작위 생성, 화면 오른쪽에서 왼쪽으로 움직임
# 3. 제일 윗 쪽에 도착 시, 거북이는 원래 위치로 돌아가고, 자동차 속도는 빨라짐
# 4. 거북이가 자동차와 충돌 시, 게임은 종료되고 모든 것이 멈춤
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.title("Over Road")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.driving()

    # Detech collision with car
    if car_manager.accident(player) :
        scoreboard.game_over()
        game_is_on = False
        
    # player reaches finish line
    if player.ycor() == FINISH_LINE_Y :
        player.clear()
        scoreboard.clear_stage()
        car_manager.level_up()

screen.exitonclick()


