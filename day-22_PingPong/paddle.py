from turtle import Turtle

class Paddle(Turtle) :

    def __init__(self, pos) :
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(pos)

    def move_up(self) :
        pos_y = self.ycor() + 20
        if pos_y < 250 :
            self.goto(self.xcor(), pos_y)

    def move_down(self) :
        pos_y = self.ycor() - 20
        if pos_y > -250 :
            self.goto(self.xcor(), pos_y)
