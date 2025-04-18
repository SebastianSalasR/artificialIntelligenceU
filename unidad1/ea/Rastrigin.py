import numpy as np
import matplotlib.pyplot as plt

class Rastrigin():

	def __get_error_surface_volume(self, *X, **kwargs):
		A = kwargs.get('A', 10)
		return A + sum([(np.square(x) - A * np.cos(2 * np.pi * x)) for x in X])


	def evaluate(self, position):
		A = 10
		return A + np.sum([(np.square(x) - A * np.cos(2 * np.pi * x)) for x in position])

	
	def get_surface(self, resolution=200, bound=3):
		
		X = np.linspace(-bound, 7, resolution)
		Y = np.linspace(-bound, bound, resolution)
				
		X, Y = np.meshgrid(X, Y)
		Z = self.__get_error_surface_volume(X, Y, A=10)
		return np.stack((X, Y, Z))


problem = Rastrigin()
surface = problem.get_surface()

fig = plt.figure(figsize=(10, 10))
plt.cla()
plt.pcolormesh(surface[0], surface[1], surface[2])
plt.show()