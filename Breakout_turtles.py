from turtle import Turtle
class Breakout(Turtle):
    def __init__(self,position,color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(position)
    def remove(self):
        self.hideturtle()
        self.clear()
        self.goto(10000,10000)
        self.remove()