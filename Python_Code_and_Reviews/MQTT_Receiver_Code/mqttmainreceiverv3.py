#Execute on Receiver Device
#V2: Added Integration with OLED and added error handling for unexpected wifi disconnect
#V3: Added integration with MQ135 Gas sensor and telemetry to GCS
import machine
from machine import Pin, ADC, PWM, I2C
from umqttsimple import MQTTClient
import math
import time
import ssd1306
from mq135 import MQ135

AIN1 = Pin(15,Pin.OUT)
AIN2 = Pin(2,Pin.OUT)
BIN1 = Pin(0,Pin.OUT)
BIN2 = Pin(4,Pin.OUT)

PWMPinA = PWM(Pin(16), freq = 980)
PWMPinB = PWM(Pin(17), freq = 980)

refresh_rate = 40 #(miliseconds)

#------------------------------------------MQ135 Init--------------------------

mq135 = MQ135(36)

#---------------------------------------------OLED Init------------------------
def clearscreen():
    oled.fill(0)
    oled.show()

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

clearscreen()
#------------------------------MQTT Init---------------------------------

oled.text('CONN MQTT...', 0, 0)
oled.show()

config = {"wifiSSID": "Пингвин Сетиь",
          "wifiPass": "Penguinnetwork",
          "ip": "192.168.43.94",
          "nodeId": "Node2"}

channel_Motor = b'/motor'
channel_telemetry= b'/telemetry'

def sub_cb(topic, msg):
    if topic == channel_Motor:
        
        clearscreen()
        
        print('Received Motor Command')
        msg = str(msg)
        print(msg)
        
        (msg, seperator, after) = msg.rpartition("'")
    

        (msg, seperator, after) = msg.rpartition("'")
    

        #First stage split
        (before, seperator, PWMB) = after.rpartition(',')
    
        #print('Quadrant: %s PWMA: %s PWMB: %s' %(mode, PWMA, PWMB))
    
        #Second stage split
        (mode, seperator, PWMA) = before.rpartition(',')
        
        oled.text('PWM A: %s'%(PWMA), 0, 0)
        oled.text('PWM A: %s'%(PWMB), 0, 10)
        

        #Conversion to integer
        mode = int(mode)
        dutyA = int(PWMA)
        dutyB = int(PWMB)
        
        
        print('PWMA: ', dutyA, 'PWMB: ', dutyB, 'Quadrant: ', mode, '\n')
     
        if mode == 1:
            ModeForward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
            oled.text('MODE: Forward', 0, 20)
             
        elif mode == 2:
            ModeBackward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
            oled.text('MODE: Backward', 0, 20)
             
        elif mode == 3:
            ModeBackward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
            oled.text('MODE: Backward', 0, 20)
             
        elif mode == 4:
            ModeForward()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
            oled.text('MODE: Forward', 0, 20)
             
        else:
            ModeStop()
            PWMPinA.duty(dutyA)
            PWMPinB.duty(dutyB)
            oled.text('MODE: Stop', 0, 20)
        
        oled.show()
            
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
oled.text('MQTT CONN EST', 0, 10)
oled.text('SUBSCRD ON:', 0, 30)
oled.text(channel_Motor, 0, 40)
oled.show()
time.sleep(3)
clearscreen()
oled.text('SYS READY:', 0, 30)
time.sleep(3)
clearscreen()
    
gasCounter = 0
ppm = 0

while True:
    
    while sta.isconnected() == False:
        clearscreen()
        oled.text('ERROR:', 0, 20)
        oled.text('GCS DISCONN', 0, 30)
        oled.text('RECONN IN 3s', 0, 40)
        time.sleep(3)
        
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.connect(config['wifiSSID'], config['wifiPass'])
        
        if sta.isconnected() == True:
            machine.reset()

    state = c.check_msg()
    
    gasCounter = gasCounter + 1
    
    if gasCounter >= 1000/refresh_rate:
        
        #Probe MQ135 Values every 1 second
        rzero = mq135.RZERO
        resistance = mq135.get_resistance()
        #print("MQ135 RZero: " + str(rzero) + "\t Resistance: "+ str(resistance) + "\t Resistance: "+ str(resistance))
        ppm = mq135.get_ppm()
        print("MQ135 RZero: " + str(rzero) + "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm))
        
        #Write telemetry to MQTT server
        #ppm = int(ppm) + 1
        ppm = str(ppm)
        c.publish(channel_telemetry, ppm)
        
        gasCounter = 0
    
    oled.text('GAS PPM: %s' %(ppm), 0, 30)
    oled.show()
    time.sleep_ms(refresh_rate)
    
    

        
    

         
         
    

