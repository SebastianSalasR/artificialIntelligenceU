from GA import Gene
import numpy as np

def evaluate(position):
    return 20 + position[0]**2 - 10 * np.cos(2 * np.pi * position[0]) + position[1]**2 - 10 * np.cos(2 * np.pi * position[1])

def main():
	# Construct the class
	ga = Gene(dna_size=2,                    # Each dna will have size elements
			dna_bounds=(-3, 7),      # DNA cannot optimise outside of these bounds
			dna_start_position=[3.1, 3.1], # DNA begins randomly around this position 
			elitism=0.5,                   # We keep the 50% fittest individuals
			population_size=500,           # We have 500 genes in the gene pool
			mutation_rate=0.01,            # Roguhly every 100 dice rolls we mutate
			mutation_sigma=0.1,            # The gene will mutated at a bound of (-0.1, 0.1)
			mutation_decay=0.999,          # The mutation size will decay each step
			mutation_limit=0.01)           # The mutation size will never get smaller than this
	
	amount_optimisation_steps = 100

	evals_to_best = 0

	# Loop and optimise each step 
	for optimisation_step in range(amount_optimisation_steps):

		# Get the current gene pool
		positions = ga.get_solutions()
		
		# Evaluate the genes using a (currently) non-existant evaluation function
		fitnesses = [evaluate(pos) for pos in positions]
		
		# Report how well each the genes performed to the
		# class, so it can internally optimise.
		ga.set_fitnesses(fitnesses)
		
		# Get the current best.
		best_position, best_fitness = ga.get_best()
		print("Best position: ", best_position)
		print("Best fitness: ", best_fitness)
		print("Evaluation to get the best position: ", evals_to_best)
		evals_to_best += 1


if __name__ == "__main__":
	main()