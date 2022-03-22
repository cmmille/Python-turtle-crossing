import turtle
from turtle import Turtle
import random
from settings import *

class Car(Turtle):
    turtle.colormode(255)
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.new_car()

    def new_car(self):
        self.rand_y()
        self.rand_x()
        self.rand_car_size()
        self.car_speed = self.rand_speed()
        self.rand_color()

    def rand_y(self):
        rand_position = random.randint(-MAX + 80, MAX - 80)
        self.sety(rand_position)

    def rand_x(self):
        rand_position = random.randint(MAX+60, MAX +100)
        self.setx(rand_position)

    def rand_car_size(self):
        car_size = random.randint(2, 5)
        self.shapesize(1, car_size)

    def rand_speed(self):
        car_speed = random.randint(2, 5)
        return car_speed

    def rand_color(self):
        r = random.randrange(50, 200, 10)
        g = random.randrange(0, 100, 10)
        b = random.randrange(50, 200, 10)
        rgb = (r, g, b)
        self.color(rgb)

    def drive(self):
        self.back(self.car_speed)

    def hit_player(self, player):
        car_size = self.shapesize()[1]*10
        car_min_x = self.xcor()-car_size
        car_max_x = self.xcor() + car_size
        car_min_y = self.ycor() - 10
        car_max_y = self.ycor() + 10
        if (car_min_x < player.xcor() < car_max_x) and (car_min_y < player.ycor() < car_max_y):
            print("hit")
            return True
        else:
            return False