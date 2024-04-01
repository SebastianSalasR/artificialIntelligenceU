import pygame
import random
import math
from ParticleClass import Particle

# Pygame Initialization
pygame.init()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

# Window dimensions
WIDTH = 944
HEIGHT = 984
domMin = -3
domMax = 7

# Window Configuration
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PSO")

# Number of particles
particles_count = 100
d = 10  # Particle diameter for display

# PSO Parameters
w = 100  # Inertia
c1 = 10  # Cognitive learning factor
c2 = 5  # Social learning factor
maxv = 0.025  # Maximum velocity
n_iters = 800  # Number of iterations

# Global best
gbestx, gbesty, gbest = 0, 0, float('inf')

# Background Image
surf = pygame.image.load("../ea/rastrigin.png")

def main():

	# Creating Particle instances
	particles = [Particle(domMin, domMax) for _ in range(particles_count)]

	# Main Loop
	running = True
	while running:
		screen.fill(BLACK)
		screen.blit(surf, (0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for particle in particles:
			particle.eval(gbest, gbestx, gbesty)
			particle.move(w, c1, c2, gbestx, gbesty, maxv, domMin, domMax)
			
			# Display the particle
			ejeX = int((domMin + particle.x) / (domMin + domMax) * WIDTH)
			ejeY = int(abs(particle.y - domMax) / (domMin + domMax) * HEIGHT)
			pygame.draw.ellipse(screen, GREEN, (ejeX, ejeY, d, d))
			pygame.draw.line(screen, BLUE, (ejeX, ejeY), (ejeX - 1000 * particle.vx, ejeY + 1000 * particle.vy), 1)

		pygame.display.flip()

	pygame.quit()
	
if __name__ == "__main__":
	main()