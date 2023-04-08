
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_shape(sides) :
    angle = 360 / sides
    for _ in range(sides):
        tim.fd(100)
        tim.right(angle)       

directions = [0, 90, 180, 270]
def draw_random(dir):
    tim.right(random.choice(directions))
    tim.fd(30)

for _ in range(1, 360, 5) :
    tim.color(random_color())
    tim.circle(100, None, None)
    tim.left(5)
    #tim.setheading(tim.heading() + gap...)

#그림판 띄우는 부분
screen = t.Screen()
screen.exitonclick()