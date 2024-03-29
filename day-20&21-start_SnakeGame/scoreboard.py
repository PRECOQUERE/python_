from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle) :
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self) :
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self) :
        if self.score > self.high_score :
            self.high_score = self.score
        self.score = 0
        self.update_score()

        