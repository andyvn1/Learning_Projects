from turtle import Turtle

with open("data.txt", mode="r") as file:
    HIGH_SCORE = int(file.read())
COLOR = "white"
SCORE_POSITION = 0, 270
ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.setposition(SCORE_POSITION)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGN, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
