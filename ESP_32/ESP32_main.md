## Working with the ESP 32

The ESP 32 is a multifunctional controller unit that can operate using many different types of firmware, granting it unique versatility to be used in a wide range of projects.

For the purposes of this project, MicroPython will be used to control the system. The specific implementations of the ESP32 utilised in this project is the ESP32-WROOM-32D and the ESP32 CAM. Both are equipped with Wifi as well as ULE Bluetooth, and comes with a host of IO pins for interfacing with sensors and other peripherals. This gives it a unique ability to interface with cloud platforms (eg. Thingspeak, AWS IoT), and in the case of the ESP32 CAM, photography and videography capability.

This page serves to provide the documentation required to set up the ESP32 microcontrollers used in the project correctly.

### General information

[Flashing Guide](../ESP_32/Flashing_Guide/esp32_flashing.md): This is mandatory for using MicroPython at all with the ESP32
>
[Pin Configuration](../ESP_32/Pin_Configuration/pinconfig.md):

[Basic IO Operations](../ESP_32)

[Description of the code used](../Python_Code_and_Reviews/software_download.md)

### Robot ESP32 specific information
[Code used](../Python_Code_and_Reviews/MQTT_Receiver_Code)

### Controller ESP32 specific information
[Code used](../Python_Code_and_Reviews/MQTT_Controller_Code)

### ESP32 CAM specific information
[Code used](../Python_Code_and_Reviews/ESP32_Cam_Code)

**Note** The ESP32 CAM runs off standard Arduino code as support for the ESP32 CAM video streaming module, as of writing, required a custom build of MicroPython. We favoured the speed of implementation over the risk of incompatibility due to time constraints. See [here](https://github.com/tsaarni/micropython-with-esp32-cam/wiki) for how to do so.
