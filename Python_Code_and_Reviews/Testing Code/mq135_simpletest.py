import time
from dht import DHT11
from machine import Pin
from mq135 import MQ135
#import mq135


# setup
mq135 = MQ135(36) # analog PIN 0

# loop
while True:
    
    rzero = mq135.RZERO
    resistance = mq135.get_resistance()
    #print("MQ135 RZero: " + str(rzero) + "\t Resistance: "+ str(resistance) + "\t Resistance: "+ str(resistance))
    ppm = mq135.get_ppm()
 

    print("MQ135 RZero: " + str(rzero) + "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm))
    time.sleep(1)