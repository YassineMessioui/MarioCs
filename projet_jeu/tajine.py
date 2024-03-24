import pygame
from images_importings import import_images


class Tajine(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 10
        self.direction = direction
        self.image = pygame.image.load(
            "./graphics/character/tajine.png"
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def go(self):
        self.rect.x += self.direction * self.speed

    def update(self, deplacement):
        self.rect.x += deplacement
