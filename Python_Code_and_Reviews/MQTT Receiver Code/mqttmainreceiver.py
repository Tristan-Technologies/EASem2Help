#Execute on Receiver Device
import machine
from machine import Pin, ADC, PWM
from umqttsimple import MQTTClient
import math
import time

AIN1 = Pin(15,Pin.OUT)
AIN2 = Pin(2,Pin.OUT)
BIN1 = Pin(0,Pin.OUT)
BIN2 = Pin(4,Pin.OUT)

PWMPinA = PWM(Pin(16), freq = 980)
PWMPinB = PWM(Pin(17), freq = 980)

config = {"wifiSSID": "Пингвин Сетиь",
          "wifiPass": "Penguinnetwork",
          "ip": "192.168.43.94",
          "nodeId": "Node2"}

channel_Motor = b'/motor'

def sub_cb(topic, msg):
    if topic == channel_Motor:
        
        print('Received Motor Command')
        msg = str(msg)
        
        (msg, seperator, after) = msg.rpartition("'")
    

        (msg, seperator, after) = msg.rpartition("'")
    

        #First stage split
        (before, seperator, PWMB) = after.rpartition(',')
    
        #print('Quadrant: %s PWMA: %s PWMB: %s' %(mode, PWMA, PWMB))
    
        #Second stage split
        (mode, seperator, PWMA) = before.rpartition(',')

        #Conversion to integer
        mode = int(mode)
        dutyA = int(PWMA)
        dutyB = int(PWMB)
        
        
        print('PWMA: ', dutyA, 'PWMB: ', dutyB, 'Quadrant: ', mode, '\n')
     
        if mode == 1:
            ModeForward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
             
        elif mode == 2:
            ModeBackward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
             
        elif mode == 3:
            ModeBackward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
             
        elif mode == 4:
            ModeForward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
             
        else:
            ModeStop()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
            
    else:
        pass
        
    
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
    
def ConnectandSubscribe():
    
    # Initializing the MQTTClient
    c = MQTTClient(config["nodeId"], config["ip"], port = 1883)

    #This function will be called when a message is received.
    #RX
    c.set_callback(sub_cb)

    #Connect to the MQTT Broker/Server.
    c.connect()

    #Subscribe to the specific topic
    c.subscribe(channel_Motor)

    print('Connected to %s MQTT broker, subscribed to %s topic' % (config["ip"], channel_Motor))
    
ConnectandSubscribe()

while True:
    
    msg = c.check_msg()
    time.sleep_ms(35)
    

        
    

         
         
    

