# In The Beginning...

At the start of the project, we had to learn the basics of MicroPython before we could move on to the actual tracked vehicle. To do so, we were given BBC micro:bit microcontrollers to learn and practice MicroPython. We were given the task to make a Space Invaders game using the 2 buttons on the micro:bit and the 5 x 5 LED grid. You can look [here](https://github.com/Tristan-Technologies/EASem2Help/tree/master/Python_Code_and_Reviews/Reviews) to see what the each of us did and what we learnt.


# Programming The Vehicle

## Part I: Movement

Armed with our newly acquired knowledge of MicroPython, we started writing the programs needed for controlling the tank. We started off with simple motor control by wiring up a L298N DC motor driver and motors together with the microcontroller, which in this case, is the ESP32 microcontroller. We were able to verify that the aforementioned components were working as intended, as well as discuss how exactly we would like our tracked vehicle moved.

After some discussion, we decided that we would use a joystick as our input device, and that we will have variable speed and directional control. In order to do so, we needed to apply some trigonometry to translate the deflection of the joystick into a vector, which has both direction (where we want to go) and magnitude (how fast we want to go) and would be decoded into a series of values to be transmitted to the robot via MQTT. The code that does the calculations is detailed [here](https://github.com/Tristan-Technologies/EASem2Help/tree/master/Python_Code_and_Reviews/MQTT_Controller_Code).

## Part II: Telemetry galore

Due to the nature of our project, we had to have wireless control and telemetry. Our robot is supposed to sniff out any dangerous gas pockets that would either blow up or suffocate any unsuspecting person that wanders into the subterranean (Or for that matter, near any entrance to the underground. There have been reports of people collapsing in front of abandoned mines from toxic gases spilling out). Thus, wireless control is the only viable option to keep people as far as possible from danger.
