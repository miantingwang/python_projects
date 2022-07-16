# import colorgram
from turtle import Turtle, Screen
from random import choice
# commented out to save running time
# colors = colorgram.extract('71RzDkIXwHL.jpeg', 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))

# color palette extracted using the colorgram module
color_list = [(249, 212, 227), (206, 214, 240), (251, 248, 222), (249, 142, 178), (100, 86, 129), (116, 86, 126),
              (90, 79, 216), (195, 141, 175), (150, 149, 188), (240, 248, 245), (208, 170, 84), (186, 180, 222),
              (239, 224, 97), (151, 110, 149), (225, 166, 24), (126, 109, 86), (22, 19, 3), (144, 210, 207),
              (241, 173, 149), (137, 169, 149), (152, 206, 214), (31, 19, 26), (96, 113, 103), (248, 239, 3),
              (85, 86, 15), (154, 117, 106), (83, 164, 102), (25, 23, 33), (9, 14, 9), (50, 150, 187)]

timmy = Turtle()
timmy.ht()


def pick_color(colors):
    color = choice(colors)
    timmy.color(color)


screen = Screen()
screen.colormode(255)

# move the turtle to the starting point
timmy.up()
timmy.goto(x=-250, y=-250)
origin = list(timmy.position())
print(origin)


def draw_dot_line():
    for _ in range(10):
        timmy.down()
        pick_color(color_list)
        timmy.dot(20)
        timmy.up()
        timmy.forward(50)


def move_up():
    global origin
    origin[1] += 50


for _ in range(10):
    draw_dot_line()
    move_up()
    timmy.goto(x=origin[0], y=origin[1])


screen.exitonclick()
