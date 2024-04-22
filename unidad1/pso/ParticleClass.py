import random
import math

class Particle:
	def __init__(self, domMin, domMax):
		self.x = random.uniform(-domMin, domMax)
		self.y = random.uniform(-domMin, domMax)
		self.px = self.x
		self.py = self.y
		self.vx = random.uniform(-1, 1)
		self.vy = random.uniform(-1, 1)
		self.pfit = float('inf')
		self.fit = float('inf')

	def eval(self, gbest, gbestx, gbesty):
		fit = 20 + self.x ** 2 - 10 * math.cos(2 * math.pi * self.x) + self.y ** 2 - 10 * math.cos(2 * math.pi * self.y)
		if fit < self.pfit:
			self.pfit = fit
			self.px = self.x
			self.py = self.y
			print(self.px, self.py)
		if fit < gbest:
			gbest = fit
			gbestx = self.x
			gbesty = self.y
		return fit

	def move(self, w, c1, c2, gbestx, gbesty, maxv, domMin, domMax):
		self.vx = w * self.vx + c1 * random.uniform(0, 1) * (self.px - self.x) + c2 * random.uniform(0, 1) * (gbestx - self.x)
		self.vy = w * self.vy + c1 * random.uniform(0, 1) * (self.py - self.y) + c2 * random.uniform(0, 1) * (gbesty - self.y)
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