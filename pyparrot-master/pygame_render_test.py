"""
	THIS FILE WILL BE USED TO DEVELOP A RENDERING SYSTEM FOR THE DRONES MOVEMENTS, AND IS TEMPORARY.
	ONCE I ACTUALLY FIGURE OUT WHAT IM DOING, I WILL DELETE THIS AND MOVE THE CODE WHEREVER
"""
import pygame
import math as m

RED = (255,0,0,255)
GREEN = (0,255,0,255)
BLUE = (0,0,255,255)
(width, height) = (300, 300)
centre = (int(width/2), int(height/2))


def main():
	global screen

	pygame.init()
	screen = pygame.display.set_mode((width, height))
	done = 0

	while not done:
		pygame.display.update()
		keys = pygame.key.get_pressed()
		pygame.draw.circle(screen, RED, centre, int(width/2))

		if keys[pygame.K_ESCAPE]:
			done = 1


		if keys[pygame.K_w]:                   #Check for w pressed
			print("W")
			pygame.draw.line(screen, BLUE, centre, (centre[0], 0), 5)


		if keys[pygame.K_a]:                   #Check for a pressed
			print("A")
			pygame.draw.line(screen, BLUE, centre, (0, centre[1]), 5)


		if keys[pygame.K_s]:                   #Check for s pressed
 			print("S")
 			pygame.draw.line(screen, BLUE, centre, (centre[0], height), 5)


		if keys[pygame.K_d]:                   #Check for d pressed
			print("D")
			pygame.draw.line(screen, BLUE, centre, (width, centre[1]), 5)

		if keys[pygame.K_UP]:
			pygame.draw.polygon(screen, BLUE, [(150,100),(100,150),(200,150)])

		if keys[pygame.K_DOWN]:
			pygame.draw.polygon(screen, BLUE, [(150,200),(200,150),(100,150)])

		if keys[pygame.K_q]:
			pygame.draw.arc(screen, BLUE, ((75,75),(75,75)), m.pi/2, m.pi, 5)

		if keys[pygame.K_e]:
			pygame.draw.arc(screen, BLUE, ((150,75),(75,75)), 0, m.pi/2, 5)


		pygame.event.pump()
		pygame.event.clear()

	print("\nMain loop broken, shutting down")
	pygame.quit()


main()
