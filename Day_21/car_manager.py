from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapetransform(2, 1)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(0, random.randint(-260, 280))
