from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() # calling the Turtle class the super class. All attributes/methods can be used here now
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_loc()

    def new_loc(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)





