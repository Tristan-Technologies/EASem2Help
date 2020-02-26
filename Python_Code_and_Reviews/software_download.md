### UGV Software Download

Here, the different versions of the software developed for the UGV can be found and downloaded. Code for testing only certain critical features/functionality (like MQTT and the OLED display) are made available for download as well. Bolded Download links indicate the latest recommended versions of that particular file.



#### Controller Unit Software (Ground Control Segement)

**[Version 1 Boot File](../Python_Code_and_Reviews/MQTT_Controller_Code/mqttbootcontroller)**:
The boot file is used to configure the preliminary connection to the router and initializes key setttings.

[Version 1 Main File](../Python_Code_and_Reviews/MQTT_Controller_Code/mqttmaincontroller):
Version 1 implements a modified form of the joystick control law which allows it to operate over MQTT. Speed and direction control is inherent to the control law already.

**[Version 2 Main File](../Python_Code_and_Reviews/MQTT_Controller_Code/mqttmaincontrollerv2)**:
Modifications were made to allow the joystick to control the camera gimbal servo motors, in tandem with a toggle switch. To reduce strain on the network, the controller was configured to transmit commands only if a change in the previous state of the joystick was detected, dramatically reducing network traffic. Refresh rate was changed as well for increased stability. Operates with Boot File V1


#### Receiver Unit Software (Vehicle)
[Version 1 Boot File](../Python_Code_and_Reviews/MQTT_Receiver_Code/mqttbootreceiver):
The boot file is used to configure the preliminary connection to the router and initializes key settings, and is functionally identical to the one used in the controller.

**[Version 2 Boot File](../Python_Code_and_Reviews/MQTT_Receiver_Code/mqttbootreceiverv2)**:
Updates to the code were made to integrate the I2C OLED Display, and display startup status updates on the screen, which aids in assessing the initialization status of the vehicle during boot up. This update requires that the OLED screen is connected at all times during the bootup process or an error will result.

[Version 1 Main File](../Python_Code_and_Reviews/MQTT_Receiver_Code/mqttmainreceiver):
Working in tandem with the Version 1 Main controller file, this implements a modified version of the joystick control law to allow for motor control over MQTT. Speed and direction control is inherent to the control law already.

[Version 2 Main File](../Python_Code_and_Reviews/MQTT_Receiver_Code/mqttmainreceiverv2):
Modifications made to provide integration with the OLED Display. Display now provides visual indication of individual motor duty cycle and operating mode.

[Version 3 Main File](../Python_Code_and_Reviews/MQTT_Receiver_Code/mqttmainreceiverv3):
Integration with MQ135 gas sensor was performed. ESP 32 now reads, and subsequently transmits the gas sensor reading (in PPM) at a regular interval over the MQTT broker to the Ground Control Station. The gas sensor reading is updated on the OLED display as well.

**[Version 4 Main File](../Python_Code_and_Reviews/MQTT_Receiver_Code/mqttmainreceiverv4)**:
In this version, integration of servo control on the receiver end was achieved. This version represents the fully functional code that was used in the demonstration of the UGV during the presentation.
