from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.pix_list = []
        self.create_snake()
        self.head = self.pix_list[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_pix = Turtle("square")
            new_pix.color("black")
            new_pix.up()
            new_pix.goto(pos)
            self.pix_list.append(new_pix)

    def move(self):
        for pix_idx in range(2, 0, -1):
            pix_corr = self.pix_list[pix_idx - 1].position()
            self.pix_list[pix_idx].goto(pix_corr)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
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
