from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed('fastest')
        random_x = randint(-250, 250)
        random_y = randint(-250, 250)
        self.goto(random_x, random_y)

    def respawn(self):
      random_x = randint(-280, 280)
      random_y = randint(-280, 280)
      self.goto(random_x, random_y)