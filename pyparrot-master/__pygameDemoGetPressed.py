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
pygame.init()

pygame.display.set_mode((250, 250))

clock = pygame.time.Clock()

while True: 
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]: 
        print("FORWARD")
    if keys[pygame.K_a]: 
        print("LEFT")
    if keys[pygame.K_s]: 
        print("BACKWARD")
    if keys[pygame.K_d]: 
        print("RIGHT")
        
    clock.tick(10) #Used to prevent spamming commands to Mambo (10 commands per second)
    
    for e in pygame.event.get(): 
        pass # proceed other events. 
             # always call event.get() or event.poll() in the main loop


