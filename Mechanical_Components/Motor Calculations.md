# Motor Calculations

When designing our UGV, we had to ascertain the necessary parameters performance parameters of our vehicle. We used the default Motor characteristics given to us as well as the following formulas for our calculations:

**Default Motor Characteristics**

Owing to the lack of information online, some of the parameters were derived experimentally through measurements.

![Motor characteristics_1](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/Default%20motor%20parameters.png)

Having established operating parameters for the motor, we are able to focus our attention on establishing performance requirements for the vehicle. 2 main requirements are defined:

1) That the maximum speed of the vehicle be above 0.9 m/s
2) That the acceleration time of the vehicle (to maximum speed) be under 3 seconds

![Motor characteristics_2](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/Motor%20parameters_2.png)
![Motor characteristics_3](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/Motor%20parameters_3.png)

**Maximum Velocity** of the vehicle can be calculated based on the angular velocity and wheel radius:

_Formula:_ ![Vmax](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/Vmax.png)

Based on a motor speed of 350rpm and a wheel radius of 2.5 cm, Vmax yields 0.91 m/s, satisfying the first requirement.

