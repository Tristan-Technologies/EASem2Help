#Tristan Technologies 2019

from numpy import interp
from numpy import 

#Homemade'setup' function


while i == 0: 
    i = i + 1
    joystickX = ADC(Pin 18)
    joystickY = ADC(Pin 20)
    
    AIN1 = Pin(15,Pin.OUT)
    AIN2 = Pin(2,Pin.OUT)
    BIN1 = Pin(0,Pin.OUT)
    BIN2 = Pin(4,Pin.OUT)

    PWMPinA = PWM(Pin(16))
    PWMPinB = PWM(Pin(17))
    
    #Bootleg Cartesian to Polar Converter
    def cart2pol(x, y):
        rho = np.sqrt(x**2 + y**2)
        phi = np.arctan2(y, x)
        return(rho, phi)
    
    def quadrant1(r, theta):  #Forward, Right
        AIN1.on()
        AIN2.off()
        BIN1.on()
        BIN2.off()
        
        joystickLimit = [0, 511]
        PWMLimit = [0, 255]
        PWMA = int(numpy.interp(r, joystickLimit, PWMLimit))  #Left Motor
        PWMB = int(PWMA * (1 - sin(theta)))                   #Right Motor
        return (PWMA, PWMB)
    
     def quadrant2(r, theta):  #Backward, Right
        AIN1.off()
        AIN2.on()
        BIN1.off()
        BIN2.on()
        
        joystickLimit = [-511, 0]
        PWMLimit = [0, 255]
        PWMA = int(numpy.interp(r, joystickLimit, PWMLimit))  #Left Motor
        PWMB = int(PWMA * (1 - sin(theta)))                   #Right Motor
        return (PWMA, PWMB)
    
    def quadrant3(r, theta):  #Backward, Left
        AIN1.off()
        AIN2.on()
        BIN1.off()
        BIN2.on()
        
        joystickLimit = [-511, 0]
        PWMLimit = [0, 255]
        PWMB = int(numpy.interp(r, joystickLimit, PWMLimit))              #Right Motor
        PWMA = int(PWMB * (1 - sin(theta)))                               #Left Motor
        return (PWMA, PWMB)
    
    
    def quadrant4(r, theta):  #Forward, Left
        AIN1.off()
        AIN2.on()
        BIN1.off()
        BIN2.on()
        
        joystickLimit = [0, 511]
        PWMLimit = [0, 255]
        PWMB = int(numpy.interp(r, joystickLimit, PWMLimit))              #Right Motor
        PWMA = int(PWMB * (1 - sin(theta)))                               #Left Motor
        return (PWMA, PWMB)
        
    



