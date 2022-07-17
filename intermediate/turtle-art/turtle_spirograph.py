from turtle import Turtle, Screen
from random import randint



# ask user for the kind of spirograph they want
n = int(input('How many circles do you want this spirograph have?: '))
if 360 % n != 0:
    print("Sorry, you have to enter a number that is a factor of 360.")

else:
    # basic setup for Turtle
    timmy = Turtle()
    timmy.speed("fastest")
    timmy.shape('turtle')
    timmy.color('brown')
    timmy.circle(100)
    screen = Screen()
    screen.colormode(255)

    def change_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        timmy.color((r, g, b))


    for _ in range(0, 361, int(360/n)):
        timmy.circle(100)
        timmy.setheading(_)
        change_color()

    screen = Screen()
    screen.exitonclick()
