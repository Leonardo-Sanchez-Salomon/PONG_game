from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-50, 330)
        self.score()

    def score(self):
        self.clear()
        self.goto(-50, 330)
        self.write(self.l_score, align="center", font=("Helvetica", 40, "normal"))
        self.goto(50, 330)
        self.write(self.r_score, align="center", font=("Helvetica", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.score()

    def r_point(self):
        self.r_score += 1
        self.score()


