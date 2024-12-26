import RPi.GPIO as GPIO
import settingUpGPIO as st
import time

motor_1 = st.Motor(22, 21, 32)
encoder_1 = st.Encoder(12, 11)
GPIO.add_event_detect(encoder_1.pinA, GPIO.RISING, encoder_1.encoder_handler)

i = 10

try:    
    while i < 101:
        i += 1
        motor_1.run("forward", i)
        print("the pwm value is: ", i, "encoder counter: ", encoder_1.counter)
        time.sleep(1)

except(KeyboardInterrupt):
    motor_1.stop()
    print("project done!!")