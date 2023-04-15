from turtle import Turtle

class Paddle(Turtle) :

    def __init__(self, pos) :
        super().__init__()
        self.step = 20
        self.make_paddle() 
        self.goto(pos)

    def make_paddle(self) :
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
                
    def go_up(self) :
        if self.ycor() < 240 :
            self.goto(self.xcor(), self.ycor() + self.step)

    def go_down(self) :
        if self.ycor() > -240  :
            self.goto(self.xcor(), self.ycor() - self.step)
