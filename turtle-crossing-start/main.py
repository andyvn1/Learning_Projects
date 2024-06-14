import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING THE STREET")
screen.tracer(0)
time_sleep = 0.1


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.write_score()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    if player.is_finish():
        scoreboard.level += 1
        time_sleep *= .5
        scoreboard.write_score()
    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor()) < 20:
            scoreboard.write_gameover()
            game_is_on = False


screen.exitonclick()
