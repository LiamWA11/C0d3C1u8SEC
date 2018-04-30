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

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Forward')
            elif event.key == pygame.K_s:
                print('Backward')
