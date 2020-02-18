# Complete project details at https://RandomNerdTutorials.com

import time
import machine
import micropython
import network
import esp
import math

config = {"wifiSSID": "YOUR_SSID_HERE",
          "wifiPass": "YOUR_PASSWORD_HERE",
          "ip": "YOUR_IP_HERE",
          "nodeId": "Node2"}

channel_Motor = b'/motor'

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(config['wifiSSID'], config['wifiPass'])



while sta.isconnected() == False:
  pass

print('Connection successful')
print(sta.ifconfig())
