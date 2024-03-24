import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((tile_size, 64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.v = vitesse_joueur
        self.gravity = GRAVITY
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = jump_speed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.face = "right"
        self.terre = False

    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def entree_joueur(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            if self.terre:
                self.jump()

    def etat_joueur(self):
        if self.direction.y < 0:
            self.status = "jumping"
        elif self.direction.y > self.gravity:
            self.status = "fall"
        elif self.direction.x != 0:
            if self.direction.x == 1:
                self.face = "right"
            else:
                self.face = "left"
            self.status = "run"
        else:
            self.status = "idle"
            if not self.terre:
                self.status = "fall"

    def update(self):
        self.entree_joueur()
        self.etat_joueur()
