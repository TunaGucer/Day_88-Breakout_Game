from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pen()
        self.hideturtle()
        self.score=0
        self.life_count=3


    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(0, 300)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))
        self.goto(100,350)
        self.write(f"Lives:{self.life_count}", align="left", font=("Courier", 30, "normal"))
        self.goto(100, 200)

    def point(self,x):
        self.score+=x
        self.update_scoreboard()

    def miss(self):
        self.life_count-=1
