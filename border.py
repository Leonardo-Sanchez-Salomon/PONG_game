from turtle import Turtle
BORDER_COLOR = "dark violet"


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor(BORDER_COLOR)
        self.penup()
        self.pensize(5)
        self.goto(x=-400, y=325)

    def line(self):
        while self.xcor() < 400:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(15)

    def draw(self):
        self.line()
        self.goto(x=-400, y=-325)
        self.line()
