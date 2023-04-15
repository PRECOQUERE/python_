from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle) :
    
    def __init__(self) :
        super().__init__()
        self.p1 = 0
        self.p2 = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write_point()
    
    def write_point(self) :
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.p2, align=ALIGN, font=FONT)        

    def l_point(self) :
        self.p1 += 1
        self.write_point()
    
    def r_point(self) :
        self.p2 += 1
        self.write_point()
        