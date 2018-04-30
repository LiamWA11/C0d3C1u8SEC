#########################################
#                                       #
#                                       #
#                                       #
#                PYGAME                 #
#                                       #
#               PYPARROT                #
#                                       #
#                                       #
#                                       #
#########################################

import pygame
import sys
from Mambo import Mambo

mamboAddr = "e0:14:d0:63:3d:d0"

pygame.init()

pygame.display.set_mode((250, 250))

mambo = Mambo(mamboAddr, use_wifi=True)

print("trying to connect")
success = mambo.connect(num_retries=3)

try:
    mambo.safe_takeoff(5)
    
    while True:
        
        keys = pygame.key.get_pressed()
        
        if keys[K_SPACE]:               #Check for space pressed
            print("SPACE")
            
            if mambo.is_landed():
                mambo.safe_takeoff(5)
            else:
                mambo.safe_land(5)
                
        if keys[K_w]:                   #Check for w pressed
            print("W")
            mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=0.1)

        if keys[K_a]:                   #Check for a pressed
            print("A")
            mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)
            
        if keys[K_s]:                   #Check for s pressed
            print("S")
            mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.1)
            
        if keys[K_d]:                   #Check for d pressed
            print("D")
            mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)
            
        if keys[K_z]:
            print("Z")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=0.1)
            
        if keys[K_x]:
            print("X")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=0.1)
            
        if keys[K_q]:
            print("Q")
            mambo.fly_direct(roll=0, pitch=0, yaw=10, vertical_movement=0, duration=0.1)
            
        if keys[K_e]:
            print("E")
            mambo.fly_direct(roll=0, pitch=0, yaw=-10, vertical_movement=0, duration=0.1)


except KeyboardInterrupt:
    print("Keboard Interrupt")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

except Exception:
    print("Error landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)
