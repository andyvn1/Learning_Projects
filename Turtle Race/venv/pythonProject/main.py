from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y_coordinate = 150

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_coordinate)
    all_turtle.append(t)
    y_coordinate -= 50

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
