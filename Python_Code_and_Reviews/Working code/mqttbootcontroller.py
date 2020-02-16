# Complete project details at https://RandomNerdTutorials.com

import time
import machine
import micropython
import network
import esp
import math
import umqttsimple

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