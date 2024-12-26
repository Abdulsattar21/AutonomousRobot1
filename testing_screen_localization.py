from turtle import Screen, Turtle
import time
import settingUpGPIO as st 
import localization as local



class Car:

    def __init__(self):
       self.car = Turtle()
       self.car.color('red')
       self.car.penup()
      # self.car("classic")
       self.speed = 0
       self.motor_1 = st.Motor(22, 21, 32) # left
       self.motor_2 = st.Motor(23, 19, 33) # right 


    def move(self, x, y, theta):
        self.car.goto(x, y)
        self.car.setheading(theta)

    def forward(self):
      self.motor_1.run("forward", 50)
      self.motor_2.run("forward", 50)
       

    def backward(self):
       self.motor_1.run("backward", 50)
       self.motor_2.run("backward", 50)
       

    def left(self):
       self.motor_2.run("forward", 50)
       self.motor_1.stop()

    def right(self):
       self.motor_2.stop()
       self.motor_1.run("forward", 50)

    def stop(self):
        self.motor_1.stop()
        self.motor_2.stop()

