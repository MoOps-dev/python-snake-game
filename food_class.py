import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(1.2)

    def spawn(self, width, height):
        width_range = random.randint(-int(width//2), int(width//2))
        height_range = random.randint(-int(height//2), int(height//2))
        self.teleport(x= float(width_range), y= float(height_range))
        self.showturtle()

    def despawn(self):
        self.clear()

    def is_visible(self):
        return self.isvisible()