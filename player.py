from turtle import Turtle
from settings import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("DarkGreen")
        self.setheading(90)
        self.sety(-MAX + 20)

    def move_up(self):
        self.forward(DIMEN / 20)

    def move_down(self):
        self.back(DIMEN / 20)
