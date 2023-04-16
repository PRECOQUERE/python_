from turtle import Turtle

class Ball(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8, 0.8)
        self.penup()
        self.step_x = 10
        self.step_y = 10
        self.speed = 0.1

    def moving(self) :
        pos_x = self.xcor() + self.step_x
        pos_y = self.ycor() + self.step_y
        self.goto(pos_x, pos_y)
                   
    def bounce_y(self) :
        self.step_y *= -1
    
    def bounce_x(self) :
        if(self.speed > 0) : self.speed -= 0.01
        self.step_x *= -1

    def reset_ball(self) :
        self.speed = 0.1
        self.goto(0,0)
        self.bounce_x()
