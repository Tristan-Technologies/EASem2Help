# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
import time
#--------------------------------------Initialisation
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


#--------------------------------------------------------------------------------------
oled.text('TristanTech 2020', 0, 0)
#oled.text('Tech 2020', 0, 10)

oled.text('AGV SYS INIT...', 0, 20)
oled.show()
time.sleep(3)
oled.text('CONN TO GCS...', 0, 30)
oled.show()
oled.text('CONN EST', 0, 40)
oled.show()
time.sleep(3)
oled.text('CONN MQTT...', 0, 50)
oled.show()
time.sleep(3)

clearscreen()
oled.text('MQTT CONN EST', 0, 0)
oled.show()
time.sleep(3)
oled.text('SYSTEM READY', 0, 10)
oled.show()
time.sleep(3)

clearscreen()
        
