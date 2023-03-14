from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("black")
        self.fillcolor("green")
        self.update()

    def update(self):
        self.goto(randint(-280, 280), randint(-280, 280))
