import colorgram
from turtle import Turtle, Screen
import random

Screen().colormode(255)
# colors = colorgram.extract("image.jpg", 30)
# rgb_list_colors = []
#
#
# first_color = colors[0]
#
# for color in colors:
#     tuple_rgb = color.rgb
#     rbg = tuple_rgb[0],tuple_rgb[1],tuple_rgb[2]
#     rgb_list_colors.append(rbg)
# print(rgb_list_colors)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

t = Turtle()
t.pensize(4)
t.speed("fastest")
y_starting_position = -250


def dotted_row(circle_in_row):
    global y_starting_position
    for _ in range(circle_in_row):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(65)
    y_starting_position += 50
    return y_starting_position


dot = True
while y_starting_position != 250:
    t.teleport(-300, y_starting_position)
    dotted_row(10)

screen = Screen()
screen.exitonclick()
