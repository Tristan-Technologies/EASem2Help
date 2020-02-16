import time
from machine import PWM, Pin

servopwm = PWM(Pin(14), freq = 50)

def interp(x, in_min, in_max, out_min, out_max):
    interpolation = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return(interpolation)

#FS90 Servo
while True:
    servopwm.duty(30) #-180
    time.sleep(5)
    servopwm.duty(123) #180
    time.sleep(5)
