import pygame
from settings import cd_but
#button class
class Button():
    
	cd = 0
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.pos = pygame.mouse.get_pos()

	def draw(self, surface):
		action = False
		#Position du souris
		Button.cd += 1
		if Button.cd > cd_but:
			self.pos = pygame.mouse.get_pos()

		#vérifier les conditions de passage de la souris et de clic
		if self.rect.collidepoint(self.pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				Button.cd = 0
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#dessiner le bouton à l'écran
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action