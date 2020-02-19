<details>
<li>
 
 [Power control circuit]</li>
 <ul>
 <li>
     
   [Boost converter](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#boost-converter)
</li>
<li>
  
  [Power calculation]()
</ul>
<li>
 
 [Electical components]
</li>
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
<li>
 
 [L298N](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#l298n)
</details>


# Power control citcuit
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/power3.png)

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/power_circuit.png)
 **Schematic Drawing**

In our power contol circuit, we have two 3.7v lithium battery. We series two 3.7v battery so that we can get 7.4v and 3000mAh total  capcitor. 
### How does the circuit work
There's one switch on the main line control the whole circutit.
The battery indicator is connecting parallel with the power source.
A boost convert is parallel connect to the battery , boost the voltage from 7.4 to 12v for the motor.
Another parallel branch connected with ESP32 by using female to male DC power adaptor.

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/adaptor.png)
**female to male DC power adaptor**

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/shield.png)
**ESP32 Shield**

### Boost converter
We use MT3608 boost converter to boost our voltage from 7.4v to 12v to power our motor.
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/boost_converter.png)

For more information about MT3608,please click [Here](https://datasheetspdf.com/pdf/909246/AEROSEMI/MT3608/1)

#### What is a Boost Converter?
A boost converter is one of the simplest types of switch mode converter. As the name suggests, it takes an input voltage and boosts or increases it. All it consists of is an inductor, a semiconductor switch (these days it’s a MOSFET, since you can get really nice ones these days), a diode and a capacitor. Also needed is a source of a periodic square wave.
The biggest advantage boost converters offer is their high efficiency – some of them can even go up to 99%! In other words, 99% of the input energy is converted to useful output energy, only 1% is wasted.

#### How Does a Boost Converter Work? 
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/Boost-Converter-2.png)

When signal source goes high, it will turning on the MOSFET. All the current is diverted through to the MOSFET through the inductor.The power source isn’t immediately short circuited since the inductor makes the current ramp up relatively slowly. Also, a magnetic field builds up around the inductor. 
The MOSFET is turned off and the current to the inductor is stopped abruptly.
Inductor responds to this by generating a large voltage with the opposite polarity of the voltage originally supplied to it using the energy stored in the magnetic field to maintain that current flow.
The inductor now acts like a voltage source in series with the supply voltage. This means that the anode of the diode is now at a higher voltage than the cathode and is forward biased.
The output capacitor is now charged to a higher voltage than before, which means that we have successfully stepped up a low DC voltage to a higher one.

# Power calculation 

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/power_consum.png)
By finding the voltage and the current draw of all our elctrical components, we find the overall power consumption which is 17.27w.
Total capacitor of our battery is 3000mAh, we suggest the derating factor is 0.85 so that we can get actual battery capacity 2550 mAh.
Since we series the circuit,the voltage of our power supply is 7.4v , hence we can find the overall available battery energy is 18.87wh by applying formula 2550mAh/1000 * 7.4v.
Here we assume the dissipative loss factor is 0.1 for the energy loss transmitted in wires.According to the data that we get, applying the formula 18.87Wh/(17.27*(1+0.1)) we can find the battery life in our prototype is 0.993h, which is 59.99mins.

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/Powe_calculation.png)

# Electrical components
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


## L298N
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/word-image-13.png)


The L298N is a dual H-Bridge motor driver which allows speed and direction control of two DC motors at the same time. The module can drive DC motors that have voltages between 5 and 35V, with a peak current up to 2A.The module has two screw terminal blocks for the motor A and B, and another screw terminal block for the Ground pin, the VCC for motor and a 5V pin which can either be an input or output.This depends on the voltage used at the motors VCC. The module have an onboard 5V regulator which is either enabled or disabled using a jumper. If the motor supply voltage is up to 12V we can enable the 5V regulator and the 5V pin can be used as output.
Here in our case ,we use 12v as external power for the motor.

Next are the logic control inputs. The Enable A and Enable B pins are used for enabling and controlling the speed of the motor. If a jumper is present on this pin, the motor will be enabled and work at maximum speed, and if we remove the jumper we can connect a PWM input to this pin and in that way control the speed of the motor. 

Next, the Input 1 and Input 2 pins are used for controlling the rotation direction of the motor A, and the inputs 3 and 4 for the motor B. Using these pins we actually control the switches of the H-Bridge inside the L298N IC. If input 1 is LOW and input 2 is HIGH the motor will move forward, and vice versa, if input 1 is HIGH and input 2 is LOW the motor will move backward.





