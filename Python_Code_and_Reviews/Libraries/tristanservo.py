#Tristan's Servo Library xd

from machine import Pin
from machine import PWM


class Servo:
  def __init__(self, pin, model):
      
    self.pwm = PWM(Pin(pin),freq=50)
    self.model = model
    
    if model == 'FS90':
        self.servoMax = 123
        self.servoMin = 30
        
    if model == 'SG90':
        self.servoMax = 102
        self.servoMin = 51
    
    self.angle(0)
    self.id = pin
    print("Initialised Servo:  %s"% (self.id))
    self.lastStat=0

  
  def angle(self,ang):
    if ang <= -90:
      ang = -90
    if ang > 90:
      ang = 90
    
    self.turn = self._map(ang,-90,90,self.servoMin,self.servoMax)
    self.pwm.duty((int)(self.turn))
    self.lastStat=ang

   
  def read(self):
    return self.lastStat
    
 
  def _map(self,x,inMin,inMax,outMin,outMax):
    return (x-inMin)*(outMax-outMin)/(inMax-inMin)+outMin

  
  def deinit(self):
    print("deinit %s"% (self.id))
    self.pwm.deinit()