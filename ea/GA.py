import numpy as np

class Gene():
	
	def __init__(self, dna_size, dna_bounds, dna_start_position=None, elitism=0.01, population_size=200, mutation_rate=0.01, mutation_sigma=0.1, mutation_decay=0.999, mutation_limit=0.01, mutate_fn=None, crossover_fn=None):
		
		self.population = self.create_random_population(dna_size, dna_bounds, population_size)
		self.population = np.clip(self.population, dna_bounds[0], dna_bounds[1])
		self.fitnesses = np.zeros_like(self.population)
		self.best_dna = None
		self.best_fitness = None
		self.dna_bounds = dna_bounds
		self.elitism = elitism
		self.population_size = population_size
		self.mutation_rate = mutation_rate
		self.mutation_sigma = mutation_sigma
		self.mutation_decay = mutation_decay
		self.mutation_limit = mutation_limit
		self.mutate_fn = mutate_fn
		self.crossover_fn = crossover_fn
		
		
	def get_solutions(self):
		self.mutation_sigma *= self.mutation_decay
		self.mutation_sigma = np.maximum(self.mutation_sigma, self.mutation_limit)
		
		return self.population
		
		
	def set_fitnesses(self, fitnesses):
		
		assert len(fitnesses) == len(self.fitnesses)
		
		self.fitnesses = np.array(fitnesses)
		
		fitnesses_indices = self.fitnesses.argsort()
		sorted_fitnesses = self.fitnesses[fitnesses_indices]
		fitnesses_weighting = np.maximum(0, 1 - sorted_fitnesses / self.fitnesses.sum())
		fitnesses_weighting /= fitnesses_weighting.sum()
		sorted_population = self.population[fitnesses_indices]
		
		self.best_dna = sorted_population[0]
		self.best_fitness = sorted_fitnesses[0]
		
		amount_new = int((1 - self.elitism) * len(self.population))
		new_population = []
		for _ in range(amount_new):

			i0 = np.random.choice(sorted_population.shape[0], p=fitnesses_weighting)
			i1 = np.random.choice(sorted_population.shape[0], p=fitnesses_weighting)

			new_dna = self.__crossover(self.population[i0], self.population[i1])
			new_dna = self.__mutate(new_dna, self.mutation_sigma, self.mutation_rate)
			new_population.append(new_dna)

		amount_old = self.population_size - amount_new
		new_population = np.array(new_population + sorted_population[:amount_old].tolist())

		assert new_population.shape == self.population.shape
		
		self.population = np.clip(new_population, self.dna_bounds[0], self.dna_bounds[1])

		
	def get_best(self):
		return self.best_dna, self.best_fitness
		
		
	def create_random_population(self, dna_size, dna_bounds, population_size):
		population = np.random.uniform(low=dna_bounds[0], high=dna_bounds[1], size=(population_size, dna_size))
		return population
	
	
	def __mutate(self, dna, mutation_sigma, mutation_rate):
		if self.mutate_fn is not None:
			return self.mutate_fn(dna)
		
		if np.random.random_sample() < mutation_rate:
			dna += np.random.standard_normal(size=dna.shape) * mutation_sigma
		
		return dna
		
	
	def __crossover(self, dna1, dna2):
		
		assert len(dna1) == len(dna2)
		
		if self.crossover_fn is not None:
			return self.crossover_fn(dna1, dna2)

		new_dna = np.copy(dna1)
		indices = np.where(np.random.randint(2, size=new_dna.size))
		new_dna[indices] = dna2[indices]
		return new_dna