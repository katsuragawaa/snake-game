from turtle import Turtle


STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:


    def __init__(self) :
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self) :
        for pos in STARTING_POS:
            self.add_segment(pos)


    def add_segment(self, position) :
        new_segment = Turtle(shape="square")
        # new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
    

    def extend(self) :
        last_pos = self.segments[-1].position()
        self.add_segment(last_pos)


    def move(self) :
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(SNAKE_SPEED)


    def up(self) :
        if self.head.heading() != DOWN :
            self.head.setheading(UP)


    def down(self) :
        if self.head.heading() != UP :
            self.head.setheading(DOWN)


    def right(self) :
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)


    def left(self) :
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)
