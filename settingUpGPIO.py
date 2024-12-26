import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


class Encoder:

    def __init__(self, pinA, pinB, radius, ticks_per_rev):
        self.pinA = pinA
        self.pinB = pinB
        self.counter = 0
        self.prev_counter = 0
        self.ticks_per_rev = ticks_per_rev
        self.radius = radius

        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def encoder_handler(self, value):
        self.prev_counter = self.counter
        if GPIO.input(self.pinB) == GPIO.input(self.pinA):
            self.counter += 1
        elif GPIO.input(self.pinB) != GPIO.input(self.pinA):
            self.counter -= 1

    def reset(self):
        self.counter = 0


class Motor:
    """
    I don't in if this going to work or not, but it is worth to try it
    maybe you need to make it in the initializing with the __init__ function (method)
    """
    model1 = []
    model2 = []

    def __init__(self, input1, input2, pwm):
        self.input1 = input1
        self.input2 = input2
        self.pwm = pwm

        ### don't forget to generate the [-100 ... 100] list to compare it with

        GPIO.setup(self.pwm, GPIO.OUT)
        GPIO.setup(self.input1, GPIO.OUT)
        GPIO.setup(self.input2, GPIO.OUT)
        self.my_pwm = GPIO.PWM(self.pwm, 100)


## also making changs here with the maximum speed

    def run(self, direction, pwm_value):

        ## make changes here as well so the input will be a speed instead of pwm signal
        # then compare it with the model and run the motor according to that
        self.direction = direction.lower()
        self.pwm_value = pwm_value
        if self.direction == "forward":
            GPIO.output(self.input1, 1)
            GPIO.output(self.input2, 0)
        elif self.direction == "backward":
            GPIO.output(self.input1, 0)
            GPIO.output(self.input2, 1)

        self.my_pwm.start(self.pwm_value)

    def stop(self):
        GPIO.output(self.input1, 0)
        GPIO.output(self.input2, 0)
        self.my_pwm.start(0)


class OneDTable:
    def __init__(self): # , motor1, motor2, encoder1, encoder2
        # self.motor1 = motor1
        # self.motor2 = motor2
        # self.encoder1 = encoder1
        # self.encoder2 = encoder2
        self.speed1 = []
        self.time1 = []

        self.dire = "forward"

    def model_motor(self, motor, encoder):
        self.motor = motor
        self.encoder = encoder

        i = 0
        prev_time = 0
        prev_counter = 0
        current_time = 0
        start_counter = 0
        timing = 0.0
        direction = 0
        while i < 101:
            current_time = time.time()
            start_counter = self.encoder.counter

            
            dcounter = start_counter - prev_counter
            timing += dt
            self.motor.run(self.dire, i)
            time.sleep(0.001)
            dt = current_time - prev_time
            

            prev_counter = start_counter
            prev_time = current_time

            self.speed1.append(dcounter/dt)
            self.time1.append(timing)
            if i > 100 and direction != 1:
                direction = 1
                self.dire = "backward"
                i = 0

            ## don't forget to manupilate the signal here like you did before

            i += 1
        return self.speed1, self.time1



