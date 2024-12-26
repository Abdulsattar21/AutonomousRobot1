from turtle import Screen, Turtle
import RPi.GPIO as GPIO
import time
import settingUpGPIO as st 
import localization as local
import plotting as plt 
import speedEstimator as speedEstimator
import testing_screen_localization as tur


car = tur.Car()
screen = Screen()
screen.setup(width=600, height = 600)
screen.title("Locaization")
screen.tracer(0)

screen.listen()
screen.onkey(car.forward, "Up")
screen.onkey(car.backward, "Down")
screen.onkey(car.left, "Left")
screen.onkey(car.right, "Right")
screen.onkey(car.stop, "space")

encoder_1 = st.Encoder(12, 11, 0.03, 300)
encoder_2 = st.Encoder(13, 15, 0.03, 300)
GPIO.add_event_detect(encoder_1.pinA, GPIO.RISING, encoder_1.encoder_handler)
GPIO.add_event_detect(encoder_2.pinA, GPIO.RISING, encoder_2.encoder_handler)
local = local.Localization(encoder_1, encoder_2, 18.1)

try:
    while True: 
        screen.update()
        time.sleep(0.1)
        x, y, theta = local.step()
        print(f"x : {x}, y : {y}, theta: {theta}")
        print(f"el.counter: {encoder_1.counter}, el.prev: {encoder_1.prev_counter}")
        print(f"er.counter: {encoder_2.counter}, er.prev: {encoder_2.prev_counter}")
        car.move(x*250, y*250, theta*250)

except(KeyboardInterrupt):
    car.stop()
