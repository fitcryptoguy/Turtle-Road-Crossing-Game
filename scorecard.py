from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.update_scorecard()


    def update_scorecard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=("Courier", 24, "normal"))



    def incrase_level(self):
        self.level = self.level + 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="Center", font=("Courier", 24, "normal"))