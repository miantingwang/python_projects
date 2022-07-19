from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
pix_list = []
for pos in starting_positions:
    new_pix = Turtle("square")
    new_pix.color("black")
    new_pix.up()
    new_pix.goto(pos)
    pix_list.append(new_pix)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for pix_idx in range(2, 0, -1):
        pix_corr = pix_list[pix_idx - 1].position()
        pix_list[pix_idx].goto(pix_corr)
    pix_list[0].forward(20)







screen.exitonclick()
