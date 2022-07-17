from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

is_game_on = True
is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

while is_game_on:
    user_input = screen.textinput(title="Welcome to the turtle race!",
                                  prompt="Pick your winner (red/orange/yellow/green/blue/purple):")
    if user_input in colors:
        is_race_on = True
        break
    elif user_input == 'off':
        is_game_on = False
    else:
        print("We don't have turtles in this color.")


turtles = []
starting_y = -100
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.up()
    new_turtle.goto(x=-220, y=starting_y)
    starting_y += 40
    turtles.append(new_turtle)

while is_race_on and is_game_on:
    for turtle_idx in range(0, 6):
        random_speed = randint(0, 10)
        turtle = turtles[turtle_idx]
        turtle.forward(random_speed)
        if turtle.xcor() >= 240:
            is_race_on = False
            print(f"The winner is the {colors[turtle_idx]} turtle!")
            if user_input == colors[turtle_idx]:
                print("You won!")
            else:
                print("You lost!")

screen.exitonclick()
