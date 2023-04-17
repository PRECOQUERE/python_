import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) :
        self.ALL_CAR = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self) :
        if random.randint(1, 6) == 6 :
            self.car = Turtle()
            self.car.shape("square")
            self.car.shapesize(1, 2)
            self.car.color(random.choice(COLORS))
            self.car.penup()
            self.car.goto(300, random.randint(-250, 250))
            self.ALL_CAR.append(self.car)

    def driving_car(self) :
        for car in self.ALL_CAR :
            car.backward(self.car_speed)
    
    # 아무리 전역변수라도 클래스 내의 메서드에선 연산해서 사용은 안되는 듯(ex: STARTING_MOVE_DISTANCE += MOVE_INCREMENT )
    def increase_speed(self) :
        self.car_speed += MOVE_INCREMENT
        
    def detect_collision(self, pos) :
        for car in self.ALL_CAR :
            if car.distance(pos) < 20 :
                return True
        
        return False