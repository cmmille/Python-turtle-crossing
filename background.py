from turtle import  Turtle
from settings import *

class Background(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setpos(x, y)

    def grass(self):
        self.shapesize(MAX/100,MAX/10)
        self.color("DarkOliveGreen3")
