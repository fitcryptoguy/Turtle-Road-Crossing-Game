from turtle import Turtle, Screen
from random import randint

car_colors = ["red", "green", "blue", "yellow", "orange", "purple", "blue", "violet", "gray", "red"]
cars = []


class Car():
    def __init__(self):
        self.car_speed = 10
        super().__init__()
        for car_color in car_colors:
            truck = Turtle()
            truck.penup()
            truck.shape("square")
            truck.color(car_color)
            truck.shapesize(stretch_wid=1, stretch_len=2)
            truck.setheading(180)
            x = randint(-270, 270)
            y = randint(-250, 250 )
            cars.append(truck)
    def traffic_control(self):
        for i in range(10):
            for j in range(10):
                if i != j:
                    if cars[i].distance(cars[j]) < 20:
                        x = cars[j].xcor()

                        y = cars[j].ycor()
                        cars[j].goto(x + 40, y + 40)

    def move(self):
        for j in cars:
            j.forward(self.car_speed)

    def repeat(self):
        for i in cars:
            if i.xcor() < -280:
                i.goto(280, randint(-270, 270))

    def speed (self ):
        self.car_speed = self.car_speed + 5

