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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if mambo.is_landed():
                        mambo.takeoff()
                    else:
                        mambo.land()
                elif event.key == pygame.K_w:
                    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=0.1)
                elif event.key == pygame.K_s:
                    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.1)
                elif event.key == pygame.K_a:
                    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)
                elif event.key == pygame.K_d:
                    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.1)
                elif event.key == pygame.K_q:
                    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-20, duration=0.1)
                elif event.key == pygame.K_e:
                    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-40,
 
 

except KeyboardInterrupt:
    print("Keboard Interrupt")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

except Exception:
    print("Error landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)
