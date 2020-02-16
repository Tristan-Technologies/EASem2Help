import machine
from machine import Pin, ADC, PWM, I2C
import umqttsimple
import math
import time
import network

counter = 0

config = {"wifiSSID": "Пингвин Сетиь",
          "wifiPass": "Penguinnetwork",
          "ip": "192.168.43.94",
          "nodeId": "Node2"}

channel_Motor = b'/motor'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config['wifiSSID'], config['wifiPass'])


while sta.isconnected() == False:
  pass

print('Connection successful')
print(sta.ifconfig())


def sub_cb(topic, msg):
    global counter
    print('Received message: %s' %(msg))
    counter = counter + 1

# Initializing the MQTTClient
c = umqttsimple.MQTTClient(config["nodeId"], config["ip"], port = 1883)

#This function will be called when a message is received.
#RX
c.set_callback(sub_cb)

#Connect to the MQTT Broker/Server.
c.connect()

#Subscribe to the specific topic
c.subscribe(channel_Motor)

while True:
    state = c.check_msg()
    print(counter)
    time.sleep_ms(20)
    
    if counter > 516:
        counter = 0
   
