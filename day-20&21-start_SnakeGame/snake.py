from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake() :
    
    def __init__(self) :
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, pos) :
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)
    
    def reset_snake(self) :
        for segment in self.segments :
            segment.goto(1000,1000)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1) :
            pos_x = self.segments[seg_num - 1].xcor()
            pos_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(pos_x, pos_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT :
            self.head.setheading(RIGHT)