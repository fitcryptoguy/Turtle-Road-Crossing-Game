from turtle import Turtle, Screen
from player import Player
import time
from Cars import Car, cars
from scorecard import Scorecard
from random import randint

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

# player

player1 = Player()
player1.color("red")


car1 = Car()
scorecard = Scorecard()


# screen listen


screen.listen()
screen.onkeypress(player1.move, "w")




game_on = True
while game_on:

    screen.update()
    time.sleep(0.07)
    car1.traffic_control()
    car1.move()
    car1.repeat()

    # check collision
    for car_objects in cars:
        if player1.distance(car_objects) < 20:
            scorecard.game_over()
            game_on = False
            print("You loose")



    # check for win
    if player1.ycor() > 280:
        print("you win")
        player1.goto(0, -270)
        car1.speed()
        scorecard.incrase_level()
        scorecard.update_scorecard()





screen.exitonclick()
