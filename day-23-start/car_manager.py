COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle

class CarManager:

    def __init__(self) :
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self) :
        random_chance = random.randint(1, 6)
        if random_chance == 6 :
            self.car = Turtle("square")
            self.car.shapesize(1,2)
            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.goto(300, random.randint(-250, 250))
            self.car.setheading(180)
            self.all_cars.append(self.car)        
    
    def driving(self) :
        for car in self.all_cars :
            car.forward(self.car_speed)

    def accident(self, pos) :
        for car in self.all_cars :
            if car.distance(pos) < 20 :
                return True
        return False
    
    def level_up(self) :
        self.car_speed += MOVE_INCREMENT
