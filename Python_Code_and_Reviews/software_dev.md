# In The Beginning...

At the start of the project, we had to learn the basics of MicroPython before we could move on to the actual tracked vehicle. To do so, we were given BBC micro:bit microcontrollers to learn and practice MicroPython. We were given the task to make a Space Invaders game using the 2 buttons on the micro:bit and the 5 x 5 LED grid. You can look [here](https://github.com/Tristan-Technologies/EASem2Help/tree/master/Python_Code_and_Reviews/Reviews) to see what the each of us did and what we learnt.


## Programming The Vehicle

### Part I: Movement

Armed with our newly acquired knowledge of MicroPython, we started writing the programs needed for controlling the tank. We started off with simple motor control by wiring up a L298N DC motor driver and motors together with the microcontroller, which in this case, is the ESP32 microcontroller. We were able to verify that the aforementioned components were working as intended, as well as discuss how exactly we would like our tracked vehicle moved.

After some discussion, we decided that we would use a joystick as our input device, and that we will have variable speed and directional control. In order to do so, we needed to apply some trigonometry to translate the deflection of the joystick into a vector, which has both direction (where we want to go) and magnitude (how fast we want to go) and would be decoded into a series of values to be transmitted to the robot. The code for the controller is detailed [here](https://github.com/Tristan-Technologies/EASem2Help/tree/master/Python_Code_and_Reviews/MQTT_Controller_Code). We started off testing our robot and controller wired together. At that point, our concern was whether the underlying programs were interpreting (on the controller) and executing (on the robot) correctly. Once that was confirmed, we went on to transition to wireless control.

### Part II: Telemetry galore

Due to the nature of our project, we had to have wireless control and telemetry. Our robot is supposed to sniff out any dangerous gases that would either blow up or suffocate any unsuspecting person that wanders into the subterranean. Thus, wireless control is the only viable option to keep people as far as possible from danger.

In order to test our concept, we decided upon using MQTT and WiFi to prove our concept in lieu of more potent wireless communication technology. We chose MQTT due to its lightweight nature and ease of setup. We made use of existing MQTT broker software available online to allow for a machine of choice (A laptop in our case) to serve as a broker. Think of a broker like a kind of server. We used [Eclipse Mosquitto](mosquitto.org) as our software of choice in this project.

We referred to [RandomNerdTutorials](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/) as a basis to build up the controller's program to be capable of decoding and transmitting the joystick inputs and the robot's program to interpret the values transmitted. Additionally, we made use of the data packets being broadcasted by the robot to piggy back gas sensor readings to the operator. The code for our robot can be found [here](https://github.com/Tristan-Technologies/EASem2Help/tree/master/Python_Code_and_Reviews/MQTT_Receiver_Code).

Subsequently, we added and ESP32 CAM to serve as the eyes, or eye if so preferred, to the robot. This required that we did a more traditional Web server as there is no possible way for MQTT, which can only broadcast short messages at best, to handle a video stream.

### Part III: Testing, Testing

With the wireless control and telemetry in place, we proceeded to test our robot. We
