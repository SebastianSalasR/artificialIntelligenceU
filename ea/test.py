import pygame
from pygame.locals import QUIT
from GA import Gene
import numpy as np
import time

# Defines Rastrigin's evaluation function
def evaluate(position):
	return 20 + position[0]**2 - 10 * np.cos(2 * np.pi * position[0]) + position[1]**2 - 10 * np.cos(2 * np.pi * position[1])

def draw_particle(screen, position):

	x = int((position[0] + 5.11) * (screen.get_width() / (2 * 5.11)))
	y = int((position[1] + 5.11) * (screen.get_height() / (2 * 5.11)))
	pygame.draw.circle(screen, (255, 0, 0), (x, y), 2)

def main():

	pygame.init()
	screen = pygame.display.set_mode((944, 984))
	pygame.display.set_caption('Rastrigin Optimization')
	clock = pygame.time.Clock()

	background = pygame.image.load('rastrigin.png')

	# Construye la clase Gene
	ga = Gene(dna_size=2,					# Each dna will have size elements
			  dna_bounds=(-3, 7),			# DNA cannot optimise outside of these bounds
			  dna_start_position=[-3, 7],	# DNA begins randomly around this position
			  elitism=0.5,					# We keep the 50% fittest individuals
			  population_size=500,			# We have 500 genes in the gene pool
			  mutation_rate=0.01,			# We have 500 genes in the gene pool
			  mutation_sigma=0.1,			# The gene will mutated at a bound of (-0.1, 0.1)
			  mutation_decay=0.999,			# The mutation size will decay each step
			  mutation_limit=0.01) 			# The mutation size will never get smaller than this

	amount_optimization_steps = 100

	counter = 0
	evals_to_best = 0
	lowest = 900000

	# Loop and optimise each step 
	for optimization_step in range(amount_optimization_steps):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				return

		# Get the current gene pool
		positions = ga.get_solutions()

		fitnesses = [evaluate(pos) for pos in positions]

		# Report how well each the genes performed to the class, so it can internally optimise.
		ga.set_fitnesses(fitnesses)

		# Get the current best.
		best_position, best_fitness = ga.get_best()

		if (best_fitness < lowest ):
			lowest = best_fitness
			evals_to_best = counter
			print("Best position: ", best_position)
			print("Best fitness: ", best_fitness)
			print("Evaluation to get the best position: ", evals_to_best)

		counter += 1

		# Dibuja las partículas en la pantalla
		screen.blit(background, (0, 0))
		for pos in positions:
			draw_particle(screen, pos)
		pygame.display.flip()

		clock.tick(30)
		
		time.sleep(.08)
	
	print("\nBest final position: ", best_position)
	print("best final fitness: ", best_fitness)
	print("Evaluation to get the best position: ", evals_to_best)
	pygame.quit()

if __name__ == "__main__":
	main()