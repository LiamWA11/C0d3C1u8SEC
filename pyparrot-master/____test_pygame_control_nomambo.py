import pygame

def main():                                        #The main game loop for the control system

    pygame.init()

    screen = pygame.display.set_mode((250, 250))

    done = 0


    try:
        while not done:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:               #Check for space pressed
                print("SPACE")

            if keys[pygame.K_w]:                   #Check for w pressed
                print("W")

            if keys[pygame.K_a]:                   #Check for a pressed
                print("A")

            if keys[pygame.K_s]:                   #Check for s pressed
                print("S")

            if keys[pygame.K_d]:                   #Check for d pressed
                print("D")

            if keys[pygame.K_z]:                   #Check for z pressed
                print("Z")

            if keys[pygame.K_x]:                   #Check for x pressed
                print("X")

            if keys[pygame.K_q]:                   #Check for q pressed
                print("Q")

            if keys[pygame.K_e]:                   #Check for e pressed
                print("E")

            if keys[pygame.K_ESCAPE]:              #Check for escape pressed, close pygame window
                print("Shutting Down \n")
                done = 1

            pygame.event.pump()
            pygame.event.clear()

        pygame.quit()


    except Exception as e:
        print("Exception: \n")
        print(str(e))



main()
