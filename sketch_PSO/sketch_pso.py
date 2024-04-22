import pygame
import random
import math

# Definición de constantes
WIDTH = 1024
HEIGHT = 512
PUNTOS = 100
D = 15
W = 1000
C1 = 30
C2 = 10
MAX_V = 3

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Clase Particle
class Particle:
	def __init__(self):
		self.x = random.randint(0, WIDTH)
		self.y = random.randint(0, HEIGHT)
		self.px = self.x
		self.py = self.y
		self.vx = random.uniform(-1, 1)
		self.vy = random.uniform(-1, 1)
		self.fit = -1
		self.pfit = -1

	def evaluar(self, surf):
		if 0 <= int(self.x) < surf.get_width() and 0 <= int(self.y) < surf.get_height():
			color = surf.get_at((int(self.x), int(self.y)))
			self.fit = color[0]  # Rojo
			if self.fit > self.pfit:
				self.pfit = self.fit
				self.px = self.x
				self.py = self.y

	def mover(self):
		self.vx = W * self.vx + random.uniform(0, 1) * (self.px - self.x) + random.uniform(0, 1) * (gbestx - self.x)
		self.vy = W * self.vy + random.uniform(0, 1) * (self.py - self.y) + random.uniform(0, 1) * (gbesty - self.y)
		modu = math.sqrt(self.vx ** 2 + self.vy ** 2)
		if modu > MAX_V:
			self.vx = self.vx / modu * MAX_V
			self.vy = self.vy / modu * MAX_V
		self.x += self.vx
		self.y += self.vy
		if self.x > WIDTH or self.x < 0:
			self.vx = -self.vx
		if self.y > HEIGHT or self.y < 0:
			self.vy = -self.vy

	def mostrar(self):
		pygame.draw.ellipse(screen, (255, 0, 0), (self.x - D/2, self.y - D/2, D, D))
		pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (self.x - 10 * self.vx, self.y - 10 * self.vy), 2)

# Función para mostrar la mejor posición
def mostrar_mejor():
	pygame.draw.ellipse(screen, (0, 0, 255), (gbestx - D/2, gbesty - D/2, D, D))
	font = pygame.font.SysFont("Arial", 15)
	text = font.render("Best fitness: {} \nEvals to best: {} \nEvals: {}".format(gbest, evals_to_best, evals), True, (0, 255, 0))
	screen.blit(text, (10, 20))

# Cargar imagen
surf = pygame.image.load("Moon_LRO_LOLA_global_LDEM_1024_b.jpg")

# Crear partículas
fl = [Particle() for _ in range(PUNTOS)]

# Variables globales
gbestx, gbesty, gbest = 0, 0, -1
evals, evals_to_best = 0, 0

# Bucle principal
running = True
while running:
	screen.fill((200, 200, 200))
	
	# Dibujar mapa y partículas
	screen.blit(surf, (0, 0))
	for p in fl:
		p.mostrar()
	mostrar_mejor()
	
	# Mover partículas y evaluar
	for p in fl:
		p.mover()
		p.evaluar(surf)
		if p.fit > gbest:
			gbest = p.fit
			gbestx, gbesty = p.x, p.y
			evals_to_best = evals
			print(gbest)
		evals += 1
	
	# Manejo de eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
