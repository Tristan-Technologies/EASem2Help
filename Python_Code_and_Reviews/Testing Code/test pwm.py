import machine
from machine import Pin, ADC, PWM
import math
import time

PWMPinB = PWM(Pin(17), freq = 980, duty = 512)