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
       Z     : ASCEND
       X     : DESCEND
       Q     : ROTATE LEFT
       E     : ROTATE RIGHT
"""

###IMPORT NECESSARY LIBRARIES
import pygame
import sys
from Mambo import Mambo
from ___functions import *


###MAMBO CLASS DEFINITION
mamboAddr = ""
mambo = Mambo(mamboAddr, use_wifi=True)
success = mambo.connect(num_retries=3)


###DEFINITION OF MAIN PYGAME LOOP FOR CONTROL SYSTEM
def main():


    ###CREATE PYGAME WINDOW AND LOOP EXIT CONDITION
    pygame.init()
    screen = pygame.display.set_mode((250, 250))
    done = 0


    try:
        while not done:

            ###GET STATE OF ALL KEYS
            keys = pygame.key.get_pressed()


            ###CHECK FOR SPECIFIC KEY INPUTS, AND ACT ACCORDINGLY
            if keys[pygame.K_SPACE]:               #Check for space pressed
                print("SPACE")

                ###CHECK FOR STATE OF DRONE, AND LAND/TAKEOFF DEPENDING ON CURRENT STATE
                if mambo.is_landed():
                    mambo.takeoff()
                else:
                    mambo.land()

            if keys[pygame.K_w]:                   #Check for w pressed
                print("W")
                ###MOVE FORWARDS
                mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=0.1)

            if keys[pygame.K_a]:                   #Check for a pressed
                print("A")
                ###STRAFE LEFT
                mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)

            if keys[pygame.K_s]:                   #Check for s pressed
                print("S")
                ###MOVE BACKWARDS
                mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.1)

            if keys[pygame.K_d]:                   #Check for d pressed
                print("D")
                ###STRAFE LEFTWARDS
                mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)

            if keys[pygame.K_z]:                   #Check for z pressed
                print("Z")
                ###ASCEND
                mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=0.1)

            if keys[pygame.K_x]:                   #Check for x pressed
                print("X")
                ###DESCEND
                mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=0.1)

            if keys[pygame.K_q]:                   #Check for q pressed
                print("Q")
                ###ROTATE ANTI-CLOCKWISE
                mambo.fly_direct(roll=0, pitch=0, yaw=10, vertical_movement=0, duration=0.1)

            if keys[pygame.K_e]:                   #Check for e pressed
                print("E")
                ###ROTATE CLOCKWISE
                mambo.fly_direct(roll=0, pitch=0, yaw=-10, vertical_movement=0, duration=0.1)

            if keys[pygame.K_ESCAPE]:              #Check for escape pressed, close pygame window
                print("Shutting Down \n")
                ###CLOSE GAME WINDOW, LAND THE DRONE
                FailsafeLand(None, mambo)
                done = 1


            ###HANDLE THE PYGAME EVENT QUEUE, ALLOWING THE PROGRAM TO INTERACT WITH THE REST OF THE OS
            pygame.event.pump()
            ###CLEAR THE EVENT QUEUE, AS EVENTS REQUIRE NO FURTHER HANDLING
            pygame.event.clear()

        pygame.quit()


    except Exception as e:
        FailsafeLand(e, mambo)


###RUN MAIN GAME LOOP
main()
