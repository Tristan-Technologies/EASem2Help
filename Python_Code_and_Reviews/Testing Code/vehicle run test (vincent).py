from machine import Pin
import time
# =====================================================================
int1 = 15 #Brown
int2 = 2  #Red
int3 = 0  #Orange
int4 = 4  #Yellow
# =====================================================================
motor1a = Pin(int1,Pin.OUT)
motor1b = Pin(int2,Pin.OUT)
motor2a = Pin(int3,Pin.OUT)
motor2b = Pin(int4,Pin.OUT)
# =====================================================================
def fwd():
    motor1a(1)
    motor1b(0)
    motor2a(1)
    motor2b(0)
def stop():
    motor1a(0)
    motor1b(0)
    motor2a(0)
    motor2b(0)
def back():
    motor1a(0)
    motor1b(1)
    motor2a(0)
    motor2b(1)  
def rotationLeft():
    motor1a(1)
    motor1b(0)
    motor2a(0)
    motor2b(1)
def rotationRight():
    motor1a(0)
    motor1b(1)
    motor2a(1)
    motor2b(0)
def rest():
    stop()
    time.sleep(1)
# =====================================================================
while True:
    fwd()
    time.sleep(0.5)
    rest()
    back()
    time.sleep(0.5)
    rest()
    rotationLeft()
    time.sleep(0.5)
    rest()
    rotationRight()
    time.sleep(0.5)
    stop()
    time.sleep(2)
    
    