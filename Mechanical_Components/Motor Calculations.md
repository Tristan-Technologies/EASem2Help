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

Based on a motor speed of 350rpm and a wheel radius of 2.5 cm, **Vmax yields 0.91 m/s**, satisfying the first requirement.


**Acceleration time requirements** To determine the torque required for acceleration (within the stipulated timeframe), it is necessary to take into account all the resistive forces that must be overcome to produce the desired acceleration. Here, we stipulate that the vehicle should be able to climb an incline of 15 degrees on a surface of concrete (mu = 0.05). To account for other inefficiencies such as bearing friction, a 10% penalty is taken on the efficiency of the system. This is done with this formula:

![Torque Formula](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/Torque-Formula.PNG)
![Torque Curve](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/torque-accel-graph.png)

Based on the above parameters and calculations, we establish that the motor torque required for acceleration under 3 seconds is **1.60 kgcm** Because the default motor provided has a torque far in excess of that (2.51 kgcm), we conclude that the motor is capable of meeting the minimum acceleration requirements.


**Validation against Maximum Tractive torque**

To prevent traction issues (ie. tracks skidding on the ground), it is necessary to ensure that the motor torque does not exceed (or exceed by too much) the Maximum Tractive Torque. Since the MTT is dependent upon friction and thus the normal reaction force of the tank, it makes sense to consider the variation of MTT for various inclination angles since that would cause the available normal reaction force acting on the vehicle to change. Thus, an expression was developed for this purpose, using the static friction coefficient for concrete (mu_s = 0.9):

![Max Tractive Torque](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/max.torque.png)
![Max Tractive Torque Curve](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Mechanical_Components/Pictures/Max%20Tractive%20torque%20graph.png)

As expected, the MTT decreases as the angle increases. At an angle of 0 degrees, the MTT available is 1.575 kgcm, below that of the motor at its rated operating torque. This indicates that the vehicle's tracks would have a propensity to skid when it firsts starts moving from rest. This was indeed observed when the vehicle was tested. Because the motor did not exceed the available MTT by too much, the skidding was still manageable and did not excessively hamper the vehicle's performance.

