## ESP 32 Pin Configuration

The primary means of interfacing the ESP 32 with other peripherals and hardware is through the 38 pins (2 sets of 19) located on the length of the board.The picture below shows the pin layout.

![Standard Pin Configuration](../Pin_Configuration/Pictures/esp32_pinout.jpg)
*Image taken from https://www.pinterest.com/pin/482940760037656205/*

Attached here is the modified version of the diagram which shows which pins that are in use by our project:

![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/ESP_32/Pin_Configuration/ESP321.png)


The particular model of the board used in this project is the ESP32-DevKitC V4. Schematics for the layout of this board are made available on Espressifs website [here](https://dl.espressif.com/dl/schematics/esp32_devkitc_v4-sch.pdf) and while not strictly necessary, these provide insight into the board's inner workings.

There are a few noteworthy pins on the board, some of which enable access to the unique functionalities afforded by this board.

# Power

It is perhaps appropriate to first discuss how the board may be powered, in the context of the pins available:

**5V & GND** - Allows the ESP32 to be powered with a 5.0 VDC power source. Making reference to the schematics, this voltage is first passed through to some form of voltage regulator (an AMS1117-3.3), which then converts and conditions the incoming supply to a stable 3.3 VDC output, after which it is distributed around the board.

**USB** - The 'normal' method of powering the board. Takes power from the USB interface and sends it to the regulator, after which it is distributed as normal.

**3V3 & GND** Pin - Allows 3.3 VDC power directly to the board. Although it may be workable in practice, after a study of the schematics, this is **not** preferred as there is no power conditioning and regulation performed by the board via this method. It is possible that the ESP32 module itself has some form of protection against unregulated power, however it is not wise to rely solely on this.

# Interfaces

Having discussed methods of powering the board, we now focus our attention to the pins available for interfacing, especially those that are more pertinent to the tracked vehicle project:

Firstly, on the advice of the manufacturer, we will be excluding the pins *D0, D1, D2, D3, CMD and CLK* as these may potentially cause interference with the board's regular operation.

**General Purpose Input/Output (GPIO)** - GPIO can be used for all digital IO operations and interfacing. This is supported by all pins, except those mentioned previously and any pin related to power.

**Analog Digital Converter (ADC)** - ADC, as the name suggest allows conversion of an Analog input to a digital input that is readable by the ESP32. This is useful for reading inputs from sensors. Pins with the *GREEN* Label are enabled with ADC functionality and can be used for such purposes.

**Digital Analog Converter (DAC)** - The DAC does the exact opposite function of the ADC: It converts digital output into an analogue one. This functionality is only available on pins 25 (GPIO25) and 26 (GPIO26)

**Pulse Width Modulation (PWM)** - PWM is used when control of intensity is required, eg. in the case of controlling motor speed or LED brightness. Fortunately the board supports PWM output on all of its GPIO pins, with the exception of course, of those mentioned at the start.

## Pin configuration of esp32 in control box:
![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/ESP_32/Pin_Configuration/ESP322.png)
This ESP32 is used in the controller unit. This ESP32 is connected to a Joystick and a toggle switch. The joystick provides the basis for generating directional commands. 2 pins are connected which monitor the voltage across the x and y axis potentiometers respectively Pins Vx and Vy) These pins are read in via the ADC.

In the process of building our prototype, we found that the Joystick is too sensitive. Thus, we designed a voltage divider circuit that we could tap off to bring the supply voltage of joystick lower to around 1v.

The toggle switch is connected to a pin which is pulled high to 3.3V when the switch is flipped. Flipping the switch allows the controller to operate in servo control mode instead of motor control.





![](https://github.com/Tristan-Technologies/EASem2Help/blob/master/ESP_32/Pin_Configuration/joystick_vsp.png)
