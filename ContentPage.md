# _CAVEBOT UGV_  :mount_fuji:

**Table of Contents**

<details>
<summary>CAVEBOT UGV</summary>
<ul>
<li>

  [Project Abstract](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Tracked-Solar-Plant.md#project-abstract)  :page_with_curl:

 </li>
<ul>
<li>

 [Introduction](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Tracked-Solar-Plant.md#introduction)
 </li>
<li>

  [Members](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Tracked-Solar-Plant.md#members)

</li>
</ul>
<li>

  [Working with the ESP 32](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Interface.md)  :bookmark_tabs:

  </li>
  <ul>
  <li><a href="https://github.com/Tristan-Technologies/EASem2Help/blob/master/ESP_32/ESP32_main.md">ESP32 Setup and Usage</a></li>
  <li>Pin Configuration</li>
  <li>Color Code</li>
  <li>Schematic Drawing </li>
  </ul>
<br>
<li>
  Working With Micropython </li>
  <ul>
    <li><a href="https://github.com/Tristan-Technologies/EASem2Help/blob/master/Python_Code_and_Reviews/Main_Python.md#python-programming">Micropython Programming</a></li>
    <li><a href="https://github.com/Tristan-Technologies/EASem2Help/blob/master/ESP_32/software_dev.md">Software Development for the UGV</a></li>
      <li><a href="https://github.com/Tristan-Technologies/EASem2Help/blob/master/ESP_32/software_download.md">UGV Software Download</a></li>
  </ul>

<br>
<li>
  Analysis of System </li>

<br>
    <li>Mechanical Components of our Vehicle</li>
      <ul>
        <li>Range and Endurance</li>
        <li>Motor Requirements</li>
        <li>Fusion360 Model</li>
        <li>Camera Gimbal</li>
      </ul>
<li>

 [Power control circuit](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#power-control-citcuit)</li>
 <ul>
 <li>

   [Boost converter](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#boost-converter)
</li>
<li>

[Power calculation]()
</ul>
<li>

[Electical components](https://github.com/Tristan-Technologies/EASem2Help/blob/master/Electrical_Components/electrical.md#electrical-components)
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
 </li>

</details>

# **Project Abstract**


In response to a need for a system that is capable of conducting unmanned reconnaissance and data gathering operations in dangerous subterranean (underground) environments like caves and mineshafts, we have developed a Unmanned Ground Vehicle that is equipped with sensors that can relay environmental conditions to human operators remotely, allowing them to make the decision if the environment is safe for humans to explore and if so, what protective measures are needed.


# **Introduction**

In the context of cave exploration or mine prospecting, it is often necessary enter the structure and collect samples, or otherwise physically survey the environment. However, these subterranean structures may harbour numerous hazards, and it is often unwise to send humans into an unknown and potentially life threatening environment right away.


There are a numerous dangers associated with such subterranean structures. One of them is the accumulation of toxic or otherwise hazardous gases inside such structures. These gases may be the result of previous human activity (as in the case of abandoned mineshafts), or due to natural processes. There are 2 direct dangers associated with such gas buildup: 1) Displacement of oxygen leading to suffocation 2) Should oxygen be present, the possibility of ignition of the flammable gas in the presence of a spark/naked flame. In very extreme cases, people have died within feet of mine openings. In either case, knowledge of the atmospheric composition of the structure would allow surveying/research teams to better equip themselves for manned exploration.

Other hazards could include low structural integrity of the cave/mineshaft, resulting in potential collapse of the structure. Any water found in the cave might also be highly acidic or alkaline, posing another hazard to humans.

In response to this, our unmanned cave exploration vehicle is equipped with a gas sensor, allowing it to detect the concentration of hazardous gases in the air. Furthermore, given that the purpose of the vehicle is to complement research, it is also equipped with a dual axis gimbaled camera (elevation and azimuth) that allows it to stream live video from the vehicle back to its control station. This aids in steering the vehicle and also allows experts to look at and use collected images or video for subsequent analysis.


## **Members**
* Camilla
* Tristan
* Yong Ziab
* Fang Qian
