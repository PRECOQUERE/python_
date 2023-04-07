from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

def draw_shape(sides) :
    angle = 360 / sides
    for _ in range(sides):
        tim.fd(100)
        tim.right(angle)       

def draw_random(dir):
    tim.right(random.choice(directions))
    tim.fd(30)

tim.ht()
tim.pensize(10)
tim.speed("fast")
for _ in range(200):
    tim.color(random.choice(colours))
    draw_random(random.randrange(1,4))

screen = Screen()
screen.exitonclick()