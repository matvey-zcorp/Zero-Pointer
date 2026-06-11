import pygame
import sys

pygame.init()

class Window:
	def __init__(self, width, height, title, icon=None):
		self.width = width
		self.height = height
		self.title = title
		self.icon = icon
		self.fullscreen = False
		self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
		pygame.display.set_caption(self.title)
		if self.icon != None:
			pygame.display.set_icon(self.icon)
	def draw(self, x, y, obj):
		self.window.blit(obj, (x, y))
	def get_width(self):
		return self.width
	def set_width(self, width):
		self.width = width
		self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
	def get_height(self):
		return self.height
	def set_height(self, height):
		self.height = height
		self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
	def get_title(self):
		return self.title
	def set_title(self, title):
		self.title = title
		pygame.display.set_caption(self.title)
	def get_icon(self):
		return self.icon
	def set_icon(self, icon):
		self.icon = icon
		pygame.display.set_icon(self.icon)
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F11:
					if not self.fullscreen:
						self.fullscreen = True
						self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.FULLSCREEN)
					else:
						self.fullscreen = False
						self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
			if event.type == pygame.QUIT:
				sys.exit()

class Image:
	def __init__(self, path):
		self.image = pygame.image.load(path).convert_alpha()
	def get_image(self):
		return self.image
	def set_size(self, width, height):
		self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (width, height))