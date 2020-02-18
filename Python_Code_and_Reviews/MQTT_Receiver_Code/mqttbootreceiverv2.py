# Complete project details at https://RandomNerdTutorials.com
#V2: Added interfacing with OLED Screen

import time
import machine
import micropython
import network
import esp
import math
from machine import Pin, I2C
import ssd1306


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

oled.text('TristanTech 2020', 0, 0)
#oled.text('Tech 2020', 0, 10)

oled.text('AGV SYS INIT...', 0, 20)
oled.show()
time.sleep(3)
#-----------------------------------------------------------------Wifi (Ground Control Segement) Init--------------------------

config = {"wifiSSID": "YOUR_SSID_HERE",
          "wifiPass": "YOUR_PASSWORD_HERE",
          "ip": "YOUR_IP_HERE",
          "nodeId": "Node2"}

channel_Motor = b'/motor'

oled.text('CONN TO GCS...', 0, 30)
oled.show()

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config['wifiSSID'], config['wifiPass'])

while sta.isconnected() == False:
  pass

oled.text('CONN EST', 0, 40)
oled.show()
print('Connection successful')
print(sta.ifconfig())
