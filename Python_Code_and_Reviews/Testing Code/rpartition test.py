#Execute on Receiver Device
import machine
from machine import Pin, ADC, PWM
import math
import time

while True:
    msg = b'0,21,32,234,634' #mode,A,B,Servo1, servo 2
    msg = str(msg)
    
    
    (msg, seperator, after) = msg.rpartition("'")
    #print(msg)

    (msg, seperator, after) = msg.rpartition("'")
    #print(after)

    (before, seperator, servo2) = after.rpartition(',')
    #print(servo2)
    
    (before, seperator, servo1) = before.rpartition(',')
    #print(servo1)
    
    (before, seperator, PWMB) = before.rpartition(',')
    #print(PWMB)
    
    (mode, seperator, PWMA) = before.rpartition(',')
    #print(PWMA)
    
    servo2 = int(servo2)
    servo1 = int(servo1)
    PWMB = int(PWMB)
    PWMA = int(PWMA)
    mode = int(mode)
    
    print(servo2)
    print(servo1)
    print(PWMB)
    print(PWMA)
    print(mode)
    #(mode, seperator, PWMA) = before.rpartition(',')
    #print(mode, PWMA, PWMB)
    
    

    time.sleep(10)
    