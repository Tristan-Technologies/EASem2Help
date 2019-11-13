# Getting started with MicroPython
As part of learning skills for ultimately working on our tracked vehicle platform, we learned about MicroPython and how to work with it. We used the ESP32 microcontroller and the BBC microbit to learn how to work with Python. We also made use of a new IDE called Thonny to do our programming in.

# Initially...
We got our hands on the BBC microbit first. It is a microcontroller designed for secondary school students in the UK to learn programming with. It was my first time working with it and it is a surprising microcontroller on its own. It has sensors like an accelerometer and compass on board, and is even capable of making use of its 5 by 5 LED grid as a sort of light sensor. However, working with it proved to bring its own set of frustrations as it was not always automatically being detected by Thonny, our IDE. Furthermore, it appears that Thonny does not have autocomplete functions unlike more sophisticated IDEs like Visual Studio or Android Studio, though I would forgive the creator since it is not a million dollar project and is open source.

# Of trials and errors
Through our introductory lesson, we learned of the many capabilities of both the IDE and microbit. The microbit is easy to underestimate, if I did not already mention it, and it turns out it had a few tricks up its sleeve. During the class, beyond basic programmes like displaying text on the microbit's LED grid, we also made use of libraries such as the Random library to carry out random number generation. We moved on to write a Space Invaders game for the microbit, making use of the library I mentioned along with the two buttons flanking the LED grid.

## Commercial break: Space Invaders assignment

As part of a task given to us, we had to write a simple Space Invaders game for the microbit. Making use of concepts learnt during our lesson using the microbit, we made a playable version of Space Invaders. Granted, it is vastly cut down in view of the limitations of the microbit. I managed to get the code running on the microbit after a number of tries, and decided to spice things up by adding score tracking to the game. I did not run into too many challenges programming, but I mainly faced the issue of structuring my logic since I was still stuck in the C++/Java style of programming where syntax involves curly braces and not whitespace. I ran into more than one error due to incorrect underlying logic, but I ultimately resolved them. You can see the code [here](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Python_Code_and_Reviews/Reviews/space_invaders.py)

# Stepping up
In our subsequent lesson, we moved on to the ESP32 microcontroller, specifically, the ESP32-WROOM-32D by Espressif. This would not be my first time working with this microcontroller, though it would be the first time that I use MicroPython on it. We were told to make use of MicroPython since it is far simpler than C++, which is what the ESP32 runs off by default, and to ensure that our friends from the non-computing related courses have a fair chance with programming the microcontroller. To flash our ESP32 microcontroller to run on MicroPython, we made use of the ESPtool by Espressif to carry out the flashing of the ESP32 microcontroller. We did however stumble a little as the commands used were meant for Unix, while we were on Windows. Fortunately, this was quickly resolved when we discovered that we only had to switch a small chunk of the commands used, specifically, from

> esptool.py --port /dev/ttyUSB0 erase_flash

to

> esptool.py --port COMxx erase_flash // Note that xx refers to the COM port number. You will see this again below for deploying the firmware

for our erase command to work.

Similarly, our flashing command required the same change and an amendment to tell the computer the filepath to the firmware instead of using the filename, which does not work on Windows.

From

> esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bi // Note the filename may vary based on firmware used

to

> esptool.py --chip esp32 --port COMxx write_flash -z 0x1000 <FILEPATH> // It is simplest to have File Explorer open besides your CLI (Command Line Interface, for the uninitiated) and to drag and drop the firmware file into the CLI to autocomplete the filepath instead of typing it out.

# Closing thoughts
Overall, I feel that this is a good starting point for me, especially as a Computer Engineering student, who will certainly learn more programming languages as I progress. I feel that there is a lot more to Python that I can potentially do, but only time will tell what I ultimately make use of.

# Resources

## Flashing the ESP32:
You can look [here](https://github.com/Tristan-Technologies/EASem2Help/tree/master/ESP_32) to see what we did

1. Tool used for flashing the ESP32: https://github.com/espressif/esptool

2. Firmware we used: https://micropython.org/resources/firmware/esp32-idf3-20191112-v1.11-576-gd667bc642.bin
*Note*: There are other firmware available that may suit your needs better. We needed LAN capabilities and thus used this firmware

## Python resources:

1. https://www.youtube.com/watch?v=nwIgxrXP-X4
Created by the man behind Thonny. Great for getting acquainted with the IDE, not so great for advanced concepts.

2. https://www.youtube.com/watch?v=rfscVS0vtbw
Extremely comprehensive guide on Python. Best taken in short blocks, for it is well over 4 hours long and I doubt many would want to sit for that long at a time.

Do note that there are some differences between Python and MicroPython. To spare you from a wall of text, you can look [here](https://docs.micropython.org/en/latest/genrst/index.html).
