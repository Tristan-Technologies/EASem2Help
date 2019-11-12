from microbit import *

# To allow for random alien craft starting points
import random
random.seed()

# Defining starting coordinates
alien_x = random.randint(0,4) # Randomise start point for alien craft
alien_y = 0
craft_x = 2

# For score keeping
score = 0

# Give the player time to get ready
display.scroll("3 2 1 GO!")

while True:

    # Re-render per cycle
    display.clear()
    display.set_pixel(craft_x, 4, 9)
    display.set_pixel(alien_x, alien_y, 5)

    # Detect user input
    if button_a.is_pressed() and craft_x > 0:
        craft_x = craft_x - 1

    if button_b.is_pressed() and craft_x < 4:
        craft_x = craft_x + 1

    # Making sure the alien craft actually moves
    alien_y = alien_y + 1

    # Sending the next alien craft after the spacecraft successfully avoids the previous alien craft and add to the player's score
    if alien_y > 4:
        alien_y = 0
        alien_x = random.randint(0,4)
        score += 1

    # Collision detection
    if alien_y == 4 and alien_x == craft_x:
        break

    # Set game speed
    sleep(250)

# End of game and score display
display.scroll("GAME OVER! SCORE: ")
display.scroll(score) # Scroll is used here in case an overly amibitious player's score exceeds 1 digit
