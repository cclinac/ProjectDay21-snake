from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.update_scoreboard()

    def reset_scoreboard(self):
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 260)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(3)
        self.clear()



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
