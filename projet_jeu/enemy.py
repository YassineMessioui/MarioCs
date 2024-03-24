import pygame
from tiles import AnimatedTile
from path import enemy_folder_path
from random import choice


class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        self.choice = choice([0, 1])
        super().__init__(size, x, y, enemy_folder_path[self.choice], 1.6)
        self.rect.y += size - self.image.get_size()[1]
        self.speed = 3

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed <= 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, screen_direction):
        self.rect.x += screen_direction
        self.animate()
        self.move()
        self.reverse_image()
