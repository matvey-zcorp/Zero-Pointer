import pygame
import sys

pygame.init()

class Window:
	def __init__(self, width, height, title, icon):
		self.width = width
		self.height = height
		self.title = title
		self.icon = icon
		self.fullscreen = False
		self.window = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
		pygame.display.set_caption(self.title)
		if self.icon != None:
			pygame.display.set_icon(self.icon)
	def draw(self, x, y, rect, obj):
		if x == None and y == None:
			self.window.blit(obj, rect)
		else:
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
		pygame.display.flip()
		self.window.fill(pygame.Color("black"))
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

class Sound:
	def __init__(self, path, loop=False):
		self.sound = pygame.mixer.Sound(path)
		self.loop = loop
	def play(self):
		if not self.loop:
			self.sound.play()
		else:
			self.sound.play(loops=-1)
	def stop(self):
		self.sound.stop()

class Button:
	def __init__(self, window, image, highlight_image, x, y, command):
		self.window = window
		self.image = image
		self.highlight_image = highlight_image
		self.command = command
		self.image_rect = self.image.get_rect(topleft=(x, y))
	def draw(self):
		if not self.image_rect.collidepoint(pygame.mouse.get_pos()):
			self.window.draw(obj=self.image, rect=self.image_rect)
		else:
			self.window.draw(obj=self.highlight_image, rect=self.image_rect)
	def update(self):
		if self.image_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
			self.command()

class Font:
	def __init__(self, path, size):
		self.font = pygame.font.Font(path, size)
		self.size = size
		self.path = path
	def get_size(self):
		return self.size
	def set_size(self):
		self.font = pygame.font.Font(self.path, size)
		self.size = size
	def get_font(self):
		return self.font
	def set_font(self, path, size):
		self.font = pygame.font.Font(path, size)

class Text:
	def __init__(self, window, x, y, font, text, smoothing, color):
		self.text = font.render(text, smoothing, color)
		self.window = window
		self.x = x
		self.y = y
		self.font = font
		self.color = color
		self.text_text = text
		self.smoothing = smoothing
		self.color
	def get_x(self):
		return self.x
	def set_x(self, x):
		self.x = x
	def get_y(self):
		return self.y
	def set_y(self, y):
		self.y = y
	def set_text(self, text):
		self.text = self.font.render(text, self.smoothing, self.color)
		self.text_text = text
	def draw(self):
		self.window.draw(obj=self.text, x=self.x, y=self.y, rect=None)