import turtle as t

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) :
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 
           
    def create_snake(self):    
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1) :
            pos_x = self.segments[seg_num - 1].xcor()
            pos_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(pos_x, pos_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #heading은 메서드기 때문에 heading()으로 사용되어야 함.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):                        
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)