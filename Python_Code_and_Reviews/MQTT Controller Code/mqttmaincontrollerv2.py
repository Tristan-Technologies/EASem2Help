#Main file for joystick controller
#V2: Added toggle switch to switch to Camera gimbal control from joystick

from machine import Pin, ADC, PWM
from umqttsimple import MQTTClient
import time
import math
import tristanservovirt

joystickX = ADC(Pin(36))
joystickY = ADC(Pin(39))
joystickX.atten(ADC.ATTN_0DB)
joystickY.atten(ADC.ATTN_0DB)
joystickX.width(ADC.WIDTH_10BIT)    #Determines value at ADC pin during joystick deflection, 10 bit provides 1024 available level states
joystickY.width(ADC.WIDTH_10BIT)

servoContPin = Pin(4,Pin.IN) #Pin for switching over to servo control mode

config = {"wifiSSID": "Пингвин Сетиь",
          "wifiPass": "Penguinnetwork",
          "ip": "192.168.43.94",
          "nodeId": "Node1"}

channel_Motor = b'/motor'

#---------------------------------------Initialise Virtual Servo library---------------------------

azimuthServo = tristanservovirt.Servo(model = 'FS90')
elevServo = tristanservovirt.Servo(model = 'FS90')

#--------------------------------Initialise joystick computation functions-------------------------

#Linear Interpolation function
def interp(x, in_min, in_max, out_min, out_max):
    interpolation = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return(interpolation)

#Bootleg Cartesian to Polar Converter Function
def cart2pol(x, y):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(x, y)
    return(rho, phi)

#Control Segements based on joystick position
def quadrant1(r, theta):  #Forward, Right

    mode = "1"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMB = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))  #Left Motor
    PWMA = int(PWMB * (1 - math.sin(theta)))                                             #Right Motor
    return (PWMA, PWMB, mode)

def quadrant2(r, theta):  #Backward, Right
    
    mode = "2"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMA = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))  #Left Motor
    PWMB = int(PWMA * (1 - math.sin(theta)))                                             #Right Motor
    return (PWMA, PWMB, mode)

def quadrant3(r, theta):  #Backward, Left
    
    mode = "3"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMB = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))              #Right Motor
    PWMA = int(PWMB * (1 + math.sin(theta)))                                                         #Left Motor
    return (PWMA, PWMB, mode)


def quadrant4(r, theta):  #Forward, Left
    
    mode = "4"
    joystickLimitMin = 0
    joystickLimitMax = 512
    PWMLimitMin = 0
    PWMLimitMax = 1023
    PWMA = int(interp(r, joystickLimitMin, joystickLimitMax, PWMLimitMin, PWMLimitMax))              #Right Motor
    PWMB = int(PWMA * (1 + math.sin(theta)))                                                         #Left Motor
    return (PWMA, PWMB, mode)

def servoControl(xcorrected, ycorrected):

    mode ='5'
    joystickLimitMin = -512
    joystickLimitMax = 512
    angleAzimuth = int(interp(xcorrected, joystickLimitMin, joystickLimitMax, -90, 90)) #Returns AZ angle based on joystick x axis
    angleElev = int(interp(ycorrected, joystickLimitMin, joystickLimitMax, -90, 90))  #Returns EL angle based on joystick y axis
    PWMA = int(azimuthServo.angle(angleAzimuth)) #AZ PWM Command for servo
    PWMB =int( elevServo.angle(angleElev)) #EL PWM Command for servo
    return (PWMA, PWMB, mode)

# Initializing the MQTTClient
c = MQTTClient(config["nodeId"], config["ip"], port = 1883)

#this function will be called when a message is received.
#TX Only
#c.set_callback(sub_cb)

#connect to the MQTT Broker/Server.
c.connect()

#subscribe to the specific topic
#c.subscribe(b'{}/msg'.format(config['nodeId']))

print('Connected to %s MQTT broker, subscribed to %s topic' % (config["ip"], channel_Motor))

while True:
    
    #Read cartesian raw value from ADC and offset
    #Update: Implemented Time averaging for Joystick signal and additional correction
    x = 0
    y = 0
    n = 0
    
    while n < 100:
        n = n + 1
        xn = joystickX.read() 
        yn = joystickY.read()
        xn = xn - 511
        yn = yn - 511
        x = x + xn
        y = y + yn
        time.sleep_us(10)
   
    X_TRIM = 119    #Additional trim variables to account for non 0 neutral reading (still abit flawed)
    Y_TRIM = 123
    
    X_THRESHOLD_MAX = 30  #Thresholds to define dead zone
    X_THRESHOLD_MIN = -30
    Y_THRESHOLD_MAX = 30
    Y_THRESHOLD_MIN = -30
    
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
    if servoContPin.value() == 1:
        (dutyA, dutyB, mode) = servoControl(xcorrected, ycorrected)
        
    elif ((0 <= theta) and (theta <= (math.pi/2))):     #0 deg < theta < 90 deg  -> Quadrant 1
        (dutyA, dutyB, mode) = quadrant1(r, theta)
        
        
    elif (((math.pi/2) < theta) and (theta <= (math.pi))):      #90 deg < theta < 180 deg  -> Quadrant 2
        (dutyA, dutyB, mode) = quadrant2(r, theta)
        
        
    elif ((-math.pi/2) > theta and theta >= -math.pi):      #180 deg < theta < 270 deg  -> Quadrant 3
        (dutyA, dutyB, mode) = quadrant3(r, theta)
        
        
    elif ((0) > theta and theta >= (-math.pi/2)):       #270 deg < theta < 360 deg  -> Quadrant 4
        (dutyA, dutyB, mode) = quadrant4(r, theta)
        
        
    else:                                                       #Motor stop if no deflection is detected/signal faulty
        mode = '0'
        dutyA = '0'
        dutyB = '0'
        
    mode = str(mode)
    dutyA = str(dutyA)
    dutyB = str(dutyB)
    command = '%s,%s,%s' %(mode, dutyA, dutyB)
    
    print('%s'%(command))
    print('%s'%(command))
    
    c.publish(channel_Motor, command)
    
    time.sleep_ms(200)
    
        
    
        
        