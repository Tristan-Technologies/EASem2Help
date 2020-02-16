import time
import machine
import micropython
import network
import esp
import math
from umqttsimple import MQTTClient

config = {"wifiSSID": "Пингвин Сетиь",
          "wifiPass": "Penguinnetwork",
          "ip": "192.168.43.94",
          "nodeId": "Node1"}

channel_Motor = b'/motor'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config['wifiSSID'], config['wifiPass'])



while sta.isconnected() == False:
  pass

print('Connection successful')
print(sta.ifconfig())

# Initializing the MQTTClient
c = MQTTClient(config["nodeId"], config["ip"], port = 1883)

#this function will be called when a message is received.
#TX Only
#c.set_callback(sub_cb)

#connect to the MQTT Broker/Server.
c.connect()

#subscribe to the specific topic
#c.subscribe(b'{}/msg'.format(config['nodeId']))

print('Connected to %s MQTT broker' % (config["ip"]))

while True:

 #-----------------------------------------------------------------------   
    mode = 0
    pwmA = 0
    pwmB = 0
    
    n = 0
    
    print('Beginning Test 1 at 3 second intervals')
    time.sleep(5)
    
    while n <= 3:
    
        mode = int(mode)
        pwmA = int(pwmA)
        pwmB = int(pwmB)
        
        pwmA = 100
        pwmB = 100
        mode = mode + 1
        n = n + 1
        
        mode = str(mode)
        pwmA = str(pwmA)
        pwmB = str(pwmB)
        
        command = '%s,%s,%s' %(mode, pwmA, pwmB)
        c.publish(channel_Motor, command)
        time.sleep(3)
        
#-----------------------------------------------------------------------      
    n = 0
    pwmA = 0
    pwmB = 0
    mode = 2
    
    print('Beginning Test 2 at 200 milisecond intervals')
    time.sleep(5)
    
    while n <= 256:
        
        mode = int(mode)
        pwmA = int(pwmA)
        pwmB = int(pwmB)
        
        pwmA = pwmA + 1
        pwmB = pwmB + 1
        n = n + 1
        
        mode = str(mode)
        pwmA = str(pwmA)
        pwmB = str(pwmB)
        
        command = '%s,%s,%s' %(mode, pwmA, pwmB)
        c.publish(channel_Motor, command)
        time.sleep_ms(200)
        
 #-----------------------------------------------------------------------    
    n = 0
    pwmA = 0
    pwmB = 0
    mode = 2
    

    print('Beginning Test 3 at 50 milisecond intervals')
    time.sleep(5)
    
    while n <= 1024:
        
        mode = int(mode)
        pwmA = int(pwmA)
        pwmB = int(pwmB)
        
        pwmA = pwmA + 1
        pwmB = pwmB + 1
        n = n + 1
        
        mode = str(mode)
        pwmA = str(pwmA)
        pwmB = str(pwmB)
        
        command = '%s,%s,%s' %(mode, pwmA, pwmB)
        c.publish(channel_Motor, command)
        time.sleep_ms(50)
        