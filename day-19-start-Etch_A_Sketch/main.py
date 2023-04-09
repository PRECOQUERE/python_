# Turtle Racing Game

#화면 크기: screen.setup(width=500, height=400)
#1.레이싱에서 첫번째로 도착할 거북이를 먼저 고름.
#2.예상이 맞았는지, 틀렸는지 마지막에 알려줌.

import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos_y = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=pos_y[turtle_index])
    all_turtles.append(new_turtle)

is_racing_on = False
if user_bat :
    is_racing_on = True

while(is_racing_on) :
    for turtle in all_turtles :
        if turtle.xcor() > 230 :
            is_racing_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bat :
                print(f"You've won! The {winner_turtle} turtle is the winner!")
            else :
                print(f"You've lost! The {winner_turtle} turtle is the winner!")
        turtle.fd(random.randint(0, 10))


screen.exitonclick()