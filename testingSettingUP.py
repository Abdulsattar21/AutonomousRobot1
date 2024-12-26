import RPi.GPIO as GPIO
import settingUpGPIO as st
import time as t 
import plotting as plt
import matplotlib.pyplot as mat


wheel_raduis = 0.03
motor_1 = st.Motor(22, 21, 32)
encoder_1 = st.Encoder(12, 11, wheel_raduis, 300 )
GPIO.add_event_detect(encoder_1.pinA, GPIO.RISING, encoder_1.encoder_handler)
plot = plt.Plot("controller", "variables", "time")

time = list(range(1, 101, 1))
list1 = list(range(1, 200, 2))
list2 = list(range(1, 300, 3))
list3 = list(range(1, 400, 4))
lists = [list1, list2, list3]
labels = ["list1", "list2", "list3"]

plot.plotting(time, lists, labels)

i = 10

try:    
    while i < 101:
        i += 1
        motor_1.run("backward", i)
        print("the pwm value is: ", i, "encoder counter: ", encoder_1.counter)
        t.sleep(1)

except(KeyboardInterrupt):
    motor_1.stop()
    print("project done!!")