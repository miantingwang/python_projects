from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.sety(275)
        self.keep_score()

    def add_score(self):
        self.score += 1
        self.keep_score()

    def keep_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
