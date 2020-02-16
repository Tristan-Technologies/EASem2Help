#Tristan Technologies 2020, Proportional-Sine (k-sine) Control Law

import machine
from machine import Pin, ADC, PWM
import math
import time

joystickX = ADC(Pin(36))
joystickY = ADC(Pin(39))
joystickX.atten(ADC.ATTN_0DB)
joystickY.atten(ADC.ATTN_0DB)
joystickX.width(ADC.WIDTH_10BIT)    #Determines value at ADC pin during joystick deflection, 10 bit provides 1024 available level states
joystickY.width(ADC.WIDTH_10BIT)


AIN1 = Pin(15,Pin.OUT)
AIN2 = Pin(2,Pin.OUT)
BIN1 = Pin(0,Pin.OUT)
BIN2 = Pin(4,Pin.OUT)

PWMPinA = PWM(Pin(16), freq = 980)
PWMPinB = PWM(Pin(17), freq = 980)

#Linear Interpolation function
def interp(x, in_min, in_max, out_min, out_max):
    interpolation = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return(interpolation)

#Bootleg Cartesian to Polar Converter Function
def cart2pol(x, y):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(x, y)
    return(rho, phi)              #rho corresponds to radial displacement (r) and phi, angular displacement (theta)

#H Bridge Mode pin config
def ModeStop():
    AIN1.off()
    AIN2.off()
    BIN1.off()
    BIN2.off()
    
def ModeForward():
    AIN1.on()
    AIN2.off()
    BIN1.on()
    BIN2.off()
    
def ModeBackward():
    AIN1.off()
    AIN2.on()
    BIN1.off()
    BIN2.on()

    
#Control Segements based on joystick position
def quadrant1(r, theta):  #Forward, Right
    
    ModeForward()
    
    mode = "Quadrant 1"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMB = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))  #Left Motor
    PWMA = int(PWMB * (1 - math.sin(theta)))                                             #Right Motor
    return (PWMA, PWMB, mode)

def quadrant2(r, theta):  #Backward, Right
    
    ModeBackward()
    
    mode = "Quadrant 2"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMA = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))  #Left Motor
    PWMB = int(PWMA * (1 - math.sin(theta)))                                             #Right Motor
    return (PWMA, PWMB, mode)

def quadrant3(r, theta):  #Backward, Left
    
    ModeBackward()
    
    mode = "Quadrant 3"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMB = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))              #Right Motor
    PWMA = int(PWMB * (1 + math.sin(theta)))                                                         #Left Motor
    return (PWMA, PWMB, mode)


def quadrant4(r, theta):  #Forward, Left
    
    ModeForward()
    
    mode = "Quadrant 4"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMA = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))              #Right Motor
    PWMB = int(PWMA * (1 + math.sin(theta)))                                                         #Left Motor
    return (PWMA, PWMB, mode)
    
    
#'main()' Function
while True:
    
    #Read cartesian raw value from ADC and offset
    #Update: Implemented Time averaging for Joystick signal and additional correction
    x = 0
    y = 0
    n = 0
    xcorrected = 0
    ycorrected = 0
    
    while n < 100:
        n = n + 1
        xn = joystickX.read() 
        yn = joystickY.read()
        xn = xn - 511
        yn = yn - 511
        #print(xn,yn)
        x = x + xn
        y = y + yn
        time.sleep_us(100)
   
    X_TRIM = 119    #Additional trim variables to account for non 0 neutral reading (still abit flawed)
    Y_TRIM = 123
    
    X_THRESHOLD_MAX = 40  #Thresholds for filtering
    X_THRESHOLD_MIN = -40
    Y_THRESHOLD_MAX = 40
    Y_THRESHOLD_MIN = -40
    
    xcorrected = -(x / 100) - X_TRIM
    ycorrected = (y / 100) + Y_TRIM
    
    if xcorrected < X_THRESHOLD_MAX and xcorrected > X_THRESHOLD_MIN:      #Filtering for signal fluctuation
        xcorrected = 0
    
    if ycorrected < Y_THRESHOLD_MAX and ycorrected > Y_THRESHOLD_MIN:
        ycorrected = 0

    if xcorrected > 512:                          #Maximum and Minimum readings
        xcorrected = 512
    
    elif xcorrected < -511:
        xcorrected = -511
        
    if ycorrected > 512:
        ycorrected = 512
    
    elif ycorrected < -511:
        ycorrected = -511
        
    
    #Compute polar coordinate from corrected cartersian value and correct again for angular (theta) and radial (r) values
    r, theta = cart2pol(xcorrected, ycorrected)
    
    if r > 512:
        r = 512
        
    #if theta < 0:
     #theta=-theta + math.pi

    #Execute control law based on quadrant position
    if ((0 <= theta) and (theta <= (math.pi/2))):     #0 deg < theta < 90 deg  -> Quadrant 1
        dutyA, dutyB, mode = quadrant1(r, theta)
        PWMPinA.duty(dutyA)
        PWMPinB.duty(dutyB)
        
    elif (((math.pi/2) < theta) and (theta <= (math.pi))):      #90 deg < theta < 180 deg  -> Quadrant 2
        dutyA, dutyB, mode = quadrant2(r, theta)
        PWMPinA.duty(dutyA)
        PWMPinB.duty(dutyB)
        
    elif ((-math.pi/2) > theta and theta >= -math.pi):      #180 deg < theta < 270 deg  -> Quadrant 3
        dutyA, dutyB, mode = quadrant3(r, theta)
        PWMPinA.duty(dutyA)
        PWMPinB.duty(dutyB)
        
    elif ((0) > theta and theta >= (-math.pi/2)):       #270 deg < theta < 360 deg  -> Quadrant 4
        dutyA, dutyB, mode = quadrant4(r, theta)
        PWMPinA.duty(dutyA)
        PWMPinB.duty(dutyB)
        
    else:                                                       #Motor stop if no deflection is detected/signal faulty
        ModeStop()
        dutyA = 0
        dutyB = 0
        PWMPinA.duty(dutyA)
        PWMPinB.duty(dutyB)



    #Debugging Lines, uncomment to enable, some use the plotter
    
    #print("x: ", x, "   y: ", y)      #512 and -512 at joystick deflection limit in either axis
    print(-511, "xcorrected: ", xcorrected, "   ycorrected: ", ycorrected, 512)

    #print()

    #print("")

    #print("r: ", r, "   theta: ", theta)  #Max R
    #print("theta: ", theta, "     Mode: ", mode)
    
    #print("")
    
    print("PWMA: ", dutyA, "   PWMB:", dutyB,    "    Mode: ", mode)
    
        
    time.sleep_ms(100) #Delay for Stability
    


    