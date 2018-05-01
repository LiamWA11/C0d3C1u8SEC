"""                 ########################################################################################################
                     _________ _______  ________  ________ _________  _____________  ______   _________________ _________
                     \_   ___ \\   _  \ \______ \ \_____  \\_   ___ \/_   |    |   \/  __  \ /   _____/\_____  \\_   ___ \ 
                     /    \  \//  /_\  \ |    |  \  _(__  </    \  \/ |   |    |   />      < \_____  \   _(__  </    \  \/ 
                     \     \___\  \_/   \|    `   \/       \     \____|   |    |  //   --   \/        \ /       \     \____
                      \______  /\_____  /_______  /______  /\______  /|___|______/ \______  /_______  //______  /\______  /
                             \/       \/        \/       \/        \/                     \/        \/        \/        \/ 
                    ########################################################################################################

CONTROL SCHEME:

       SPACE : TAKEOFF/LAND
       W     : FLY FORWARDS
       A     : SRAFE LEFT
       S     : STRAFE RIGHT
       D     : FLY BACKWARDS
       UP    : ASCEND
       DOWN  : DESCEND
       Q     : ROTATE LEFT
       E     : ROTATE RIGHT
"""

###IMPORT NECESSARY LIBRARIES
import sys
import math as m
import pygame
from Mambo import Mambo
from ___functions import *

###PYGAME DISPLAY DEFINITIONS
RED = (255,0,0,255)
GREEN = (0,255,0,255)
BLUE = (0,0,255,255)
(width, height) = (300, 300)
centre = (int(width/2), int(height/2))

###MAMBO CLASS DEFINITION
mamboAddr = ""
mambo = Mambo(mamboAddr, use_wifi=True)
success = mambo.connect(num_retries=3)


###DEFINITION OF MAIN PYGAME LOOP FOR CONTROL SYSTEM
def main():


    ###CREATE PYGAME WINDOW AND LOOP EXIT CONDITION
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    done = 0

    try:
        while not done:
            ###UPDATE THE DISPLAY, WRITE THE CIRCLE AGAIN TO "DELETE" SHAPES THAT AREN'T NECESSARY
            pygame.display.update()
            pygame.draw.circle(screen, RED, centre, int(width/2))
            ###GET STATE OF ALL KEYS
            keys = pygame.key.get_pressed()
            ###DEFINE AND/OR RESET MOVEMENT VARIABLES
            roll, pitch, yaw, vert = 0, 0, 0, 0

            ###CHECK FOR SPECIFIC KEY INPUTS, AND MODIFY MOVEMENT VARIABLES/DRAW SHAPES ACCODINGLY

            if keys[pygame.K_SPACE]:               #Check for space pressed
                ###CHECK FOR STATE OF DRONE, AND LAND/TAKEOFF DEPENDING ON CURRENT STATE
                if mambo.is_landed():
                    mambo.safe_takeoff(2)
                    mambo.smart_sleep(1)

                else:
                    mambo.safe_land(2)
                    mambo.smart_sleep(1)

            if keys[pygame.K_w]:                   #Check for w pressed
                ###MOVE FORWARDS
                pitch = 50
                ###DRAW A LINE TOWARDS THE TOP OF SCREEN
                pygame.draw.line(screen, BLUE, centre, (centre[0], 0), 5)

            if keys[pygame.K_a]:                   #Check for a pressed
                ###STRAFE LEFT
                roll = -50
                ###DRAW A LINE TOWARDS THE LEFT OF SCREEN
                pygame.draw.line(screen, BLUE, centre, (0, centre[1]), 5)

            if keys[pygame.K_s]:                   #Check for s pressed
                ###MOVE BACKWARDS
                pitch = -50
                ###DRAW A LINE TOWARDS THE BOTTOM OF SCREEN
                pygame.draw.line(screen, BLUE, centre, (centre[0], height), 5)

            if keys[pygame.K_d]:                   #Check for d pressed
                ###STRAFE LEFTWARDS
                roll = 50
                ###DRAW A LINE TOWARDS THE RIGHT OF THE SCREEN
                pygame.draw.line(screen, BLUE, centre, (width, centre[1]), 5)

            if keys[pygame.K_UP]:                   #Check for UP arrow pressed
                ###ASCEND
                vert = 50
                ###DRAW AN UPWARDS FACING TRIANGLE
                pygame.draw.polygon(screen, BLUE, [(150, 100), (100, 150), (200, 150)])

            if keys[pygame.K_DOWN]:                   #Check for DOWN arrow pressed
                ###DESCEND
                vert = -50
                ###DRAW A DOWNWARDS FACING TRIANGLE
                pygame.draw.polygon(screen, BLUE, [(150, 200), (200, 150), (100, 150)])

            if keys[pygame.K_q]:                   #Check for q pressed
                ###ROTATE ANTI-CLOCKWISE
                yaw = 50
                ###DRAW AN ARC ON THE LEFT OF THE SCREEN
                pygame.draw.arc(screen, BLUE, ((75, 75), (75, 75)), m.pi/2, m.pi, 5)

            if keys[pygame.K_e]:                   #Check for e pressed
                ###ROTATE CLOCKWISE
                yaw = -50
                ###DRAW AN ARC ON THE RIGHT OF THE SCREEN
                pygame.draw.arc(screen, BLUE, ((150, 75), (75, 75)), 0, m.pi/2, 5)

            if keys[pygame.K_ESCAPE]:              #Check for escape pressed, close pygame window
                print("Shutting Down \n")
                ###BREAK GAME LOOP, LAND THE DRONE
                FailsafeLand("Pygame window closed with escape.", mambo)
                done = 1

            ###TELL THE DRONE TO MOVE AS ACCORDING TO MOVEMENT VARIABLES
            mambo.fly_direct(roll, pitch, yaw, vert, duration=0.05)
            ###HANDLE THE PYGAME EVENT QUEUE, ALLOWING THE PROGRAM TO INTERACT
            ###WITH THE REST OF THE OS
            pygame.event.pump()
            ###CLEAR THE EVENT QUEUE, AS EVENTS REQUIRE NO FURTHER HANDLING
            pygame.event.clear()
            ###PAUSE THE PROGRAM FOR 0.05 SECONDS (THE DURATION OF A SINGLE COMMAND) SO
            ###THAT THE COMMANDS DO NOT STACK
            pygame.time.wait(50)

        ###QUIT THE PYGAME WINDOW IF THE LOOP IS BROKEN
        pygame.quit()


    except Exception as error:
        FailsafeLand(error, mambo)


###RUN MAIN GAME LOOP
main()
