from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.write_score()

    def write_score(self) :
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.score2, align=ALIGN, font=FONT)

    def plus_s1(self):
        self.score1 += 1
        self.write_score()

    def plus_s2(self) :
        self.score2 += 1
        self.write_score()

        