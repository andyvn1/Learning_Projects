from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

user1_paddle = Paddle(350, 0)
user2_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(user1_paddle.up, "Up")
screen.onkeypress(user1_paddle.down, "Down")
screen.onkeypress(user2_paddle.up, "w")
screen.onkeypress(user2_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(user1_paddle) < 60 and ball.xcor() > 320 or ball.distance(user2_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    #User 1 Paddle
    if ball.xcor() > 380:
        ball.reset_home()
        scoreboard.l_point()
        
    #User 2 paddle
    if ball.xcor() < -380:
        ball.reset_home()
        scoreboard.r_point()










screen.exitonclick()
