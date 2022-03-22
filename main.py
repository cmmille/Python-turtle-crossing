from turtle import Screen
from player import Player
from background import Background
from message import Message
from car import Car
from settings import *
import time

# Setup screen
screen = Screen()
screen.setup(width=DIMEN, height=DIMEN)
screen.bgcolor("DarkGray")
screen.tracer(False)
bottom_grass = Background(0, -MAX+30).grass()
top_grass = Background(0, MAX-30).grass()

# Create message
message = Message()

# Create player
player = Player()

# Create cars
cars = []
for i in range(0, 21):
    car = Car()
    cars.append(car)

# Listeners
screen.listen()
screen.onkey(key="Up", fun = player.move_up)
screen.onkey(key="w", fun = player.move_up)
screen.onkey(key="Down", fun = player.move_down)
screen.onkey(key="s", fun = player.move_down)


game_over = False
while not game_over:
    time.sleep(0.0025)
    screen.update()
    for car in cars:
        car.drive()
        if car.xcor() < -MAX-60:
            car.new_car()
        hit = car.hit_player(player)
        if hit:
            game_over = True
            message.lose()

    if player.ycor() > MAX - 30:
        game_over = True
        message.win()
screen.exitonclick()