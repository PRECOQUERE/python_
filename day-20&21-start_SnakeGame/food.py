from turtle import Turtle
import random

class Food(Turtle) :
    
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.move_position()
        
    def move_position(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x, pos_y)