import RPi.GPIO as GPIO
import sensorInterruption as sensor

class Encoder: 
    def __init__(self, pinA, pinB, ticks_per_revol, raduis):
        self.counter = 0 
        self.pinA = pinA
        self.pinB = pinB
        self.ticks_per_revol = ticks_per_revol
        self.raduis =raduis
        sensor.SensorInterruption(self.pinA, self.pinB, Encoder.encoder_handler)
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setup(pinA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # GPIO.setup(pinB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # GPIO.add_event_detect(pinA, GPIO.RISING, Encoder.encoder_handler)


    def encoder_handler(self):
        if GPIO.input(self.pinA) == GPIO.input(self.pinB): 
            self.counter += 1 
        elif GPIO.input(self.pinA) != GPIO.input(self.pinB):
            self.counter -= 1 
        print(self.counter)
    
    def reset(self):
        self.counter = 0