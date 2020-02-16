import tristanservo
import time
sv1 = tristanservo.Servo(14, model = 'FS90')
#sv2 = Servo.Servo(pin=13)
time.sleep(1)

try:
  while True:
    sv1.angle(0)
    time.sleep(2)
    
    sv1.angle(-90)
    time.sleep(2)
    
    sv1.angle(90)
    time.sleep(2)
except:
  sv1.deinit()
  #sv2.deinit()