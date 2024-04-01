import pygame
import random
import math

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

# Dimensiones de la ventana
WIDTH = 600
HEIGHT = 600
domMin = -3
domMax = 7

# Configuración de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PSO")

# Cantidad de partículas
puntos = 100
d = 10  # Diámetro de la partícula para mostrar

# Parámetros PSO
w = 500  # Inercia
C1 = 5  # Factor de aprendizaje propio
C2 = 500  # Factor de aprendizaje social
maxv = 0.025  # Velocidad máxima
n_iters = 800  # Número de iteraciones

# Mejor global
gbestx, gbesty, gbest = 0, 0, float('inf')

# Imagen de fondo
surf = pygame.image.load("rastrigin_dom.png")

# Creación de la clase Particle
class Particle:
	def __init__(self):
		self.x = random.uniform(-domMin, domMax)
		self.y = random.uniform(-domMin, domMax)
		self.px = self.x
		self.py = self.y
		self.vx = random.uniform(-1, 1)
		self.vy = random.uniform(-1, 1)
		self.pfit = float('inf')
		self.fit = float('inf')

	def eval(self):
		global gbest, gbestx, gbesty
		fit = 20 + self.x ** 2 - 10 * math.cos(2 * math.pi * self.x) + self.y ** 2 - 10 * math.cos(2 * math.pi * self.y)
		if fit < self.pfit:
			self.pfit = fit
			self.px = self.x
			self.py = self.y
		if fit < gbest:
			gbest = fit
			gbestx = self.x
			gbesty = self.y
			print(gbestx, gbesty)
		return fit

	def move(self):
		global w
		self.vx = w * self.vx + random.uniform(0, 1) * (self.px - self.x) + random.uniform(0, 1) * (gbestx - self.x)
		self.vy = w * self.vy + random.uniform(0, 1) * (self.py - self.y) + random.uniform(0, 1) * (gbesty - self.y)
		modu = math.sqrt(self.vx ** 2 + self.vy ** 2)
		if modu > maxv:
			self.vx = self.vx / modu * maxv
			self.vy = self.vy / modu * maxv
		self.x += self.vx
		self.y += self.vy
		if self.x > domMax or self.x < -domMin:
			self.vx = -self.vx
		if self.y > domMax or self.y < -domMin:
			self.vy = -self.vy

	def display(self):
		ejeX = int((domMin + self.x) / (domMin + domMax) * WIDTH)
		ejeY = int(abs(self.y - domMax) / (domMin + domMax) * HEIGHT)
		pygame.draw.ellipse(screen, GREEN, (ejeX, ejeY, d, d))
		pygame.draw.line(screen, BLUE, (ejeX, ejeY), (ejeX - 1000 * self.vx, ejeY + 1000 * self.vy), 1)

# Creación de las partículas
fl = [Particle() for _ in range(puntos)]

# Bucle principal
running = True
while running:
	screen.fill(BLACK)
	screen.blit(surf, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for p in fl:
		p.display()
		p.move()
		p.eval()

	pygame.display.flip()

pygame.quit()