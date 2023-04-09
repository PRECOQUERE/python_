# Drawing with Turtle

import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.backward(10)

def ct_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear() :
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(move_forwards, "space")
screen.onkey(move_backwards, "s")
screen.onkey(ct_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()

