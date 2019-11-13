#Tristan Technologies 2019

from microbit import *
import random

random.seed()

#Spaceship coordinate variables, sc_y is not needed as it is fixed
sc_x = 2

#Alien coordinate variable, ac_x is initialised using the RNG
#ac_y is propagated along y axis each program cycle, to give the impression of falling down
ac_x = random.randint(0,4)
ac_y = 0


while True:
    
    #Re render alien and spaceship on LED Matrix each program cycle
    display.clear()
    display.set_pixel(sc_x, 4, 9)
    display.set_pixel(ac_x, ac_y, 5)
    
    #Check for changes to SC position
    #Inequalities are provided to prevent illegal values of sc_x
    if button_a.is_pressed() and sc_x > 0:
        sc_x = sc_x - 1
        
    if button_b.is_pressed() and sc_x < 4:
        sc_x = sc_x + 1
      
    #Alien y propagation   
    ac_y = ac_y + 1
    
    #Alien y coordinate zeroing after falling to the end of matrix
    #and Alien x coordinate reinitialization
    if ac_y > 4:
        ac_y = 0
        ac_x = random.randint(0,4)
    
    #Collision verification routine
    if ac_y == 4 and ac_x == sc_x:
        break
        
    sleep(250)
    

#Display message if collision detected
display.scroll("GAME OVER BLYAT", loop = True)