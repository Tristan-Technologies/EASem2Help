<details>
<summary>Power control circuit</summary>
 <ul>
 <li>
     
   [Boost converter]()
</li>
<li>
  
  [Power calculation]()
</ul>
<summary>Electical components</summary>
<ul>
<li>

  [MQ135](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#mq135)  

 </li>
 <li>
  
   [Battery indicator](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#battery-indicator)  
</li>
<ul>
  <li>
    
   [TL431 Voltage Monitor Circuit](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#tl431-voltage-monitor-circuit)
  </li>
  
</ul>
<li>
  
  [Joystick](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#joystick)
  
</li>

</details>


# Power control citcuit
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/power2.png)

In our power contol circuit, we have two 3.7v lithium battery. We series two 3.7v battery so that we can get 7.4v and 3000mAh total  capcitor.

# MQ135

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/MQ135.png)

MQ135 is the gas sensor that we used for our prototype.

### How it works:
the gas sensitive material used in the MQ135 gas sensor is tin dioxide (SnO2) with low conductivity in clean air. When there is polluted gas in the environment, the conductivity of the sensor increases with the concentration of polluted gas in the air. The MQ135 gas sensor is highly sensitive to ammonia, sulfide, benzene vapor, and ideal for monitoring smog and other hazardous gases. This sensor can detect a variety of harmful gases, is a low-cost sensor suitable for a variety of applications.
Here is the circuit in MQ135:

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/Gas_sensor.png)

For more information,please click [Here](http://www.waveshare.net/w/upload/2/24/MQ-135-Gas-Sensor-UserManual.pdf)

# Battery indicator
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/battery_indicator.png)

The mode of our battery indicator is SPBKBS - 10.We use a battery indicator in our prototype to show the battery level.
 It will be easier for user to see how much battery charge remaining.
 
 This battery indicator has eight pads correspond to different voltages . In our case, the voltage of power supply is 7.4v ( two 3.7v lithium battery connected in series) so we choose the second pad.
 
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/back_battery_indicator.png)


## TL431 Voltage Monitor Circuit
For SPBKBS - 10, it uses TL431 inside.
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/Zener.pngx.png)
A TL431 is an Adjustable Precision Zener Shunt Regulator. Its output voltage can be set to any value between 2.5V and 36V with the use of two external resistors.


![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/TL431_c.png)

Above is shown the standard circuit diagram for a TL431-based voltage monitor. The aim of the monitor is simply to light up an LED when a target voltage is reached 

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/forumula.png)


The simple equation displayed above gives the high limit – in this case the voltage at which the LED will light up. Since the reference voltage (Vref) is fixed at 2.5 Volts in the TL431, the resistors R1 and R2 (which form a voltage divider) are selected to provide the desired high limit voltage.
For example,if we use R1 =2.21K, R2=1K ,by applying the formulea, we can get hight limit to 7.8v ,in this case , all four leds will light up and indicate that our batter is fully charged.

## Joystick 
Our group use Joystick to control our motor and servo.
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/joystick.jpg)

How this works

The joystick in the picture is nothing but two potentiometers that allow us to messure the movement of the stick in 2-D. Potentiometers are variable resistors and, in a way, they act as sensors providing us with a variable voltage depending on the rotation of the device around its shaft.

The kind of program that we need to monitor the joystick has to make a polling to two of the analog pins. We can send these values back to the computer, but then we face the classic problem that the transmission over the communication port has to be made with 8bit values, while our DAC (Digital to Analog Converter - that is messuring the values from the potentiometers in the joystick) has a resolution of 10bits. In other words this means that our sensors are characterized with a value between 0 and 1024.

The following code includes a method called treatValue() that is transforming the sensor's messurement into a value between 0 and 9 and sends it in ASCII back to the computer. This allows to easily send the information into e.g. Flash and parse it inside your own code.







