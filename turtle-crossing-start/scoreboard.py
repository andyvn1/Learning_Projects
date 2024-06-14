from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0

    def write_gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def write_score(self):
        self.clear()
        self.goto(x=-270, y=265)
        self.write(f"Level: {self.level}", align="left", font=FONT)
