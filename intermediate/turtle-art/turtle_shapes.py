from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape('turtle')
timmy.color('brown')
timmy.width(5)
timmy.speed(0)
screen = Screen()
screen.colormode(255)


def draw_shape():
    turning_angle = 360/n
    for _ in range(n):
        timmy.forward(100)
        timmy.right(turning_angle)


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    timmy.color((r, g, b))


def random_direction():
    angle = [0, 90, 180, 270]
    return choice(angle)


for _ in range(200):
    timmy.setheading(random_direction())
    timmy.forward(20)
    change_color()

screen.exitonclick()