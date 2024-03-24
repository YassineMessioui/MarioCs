import pygame
from settings import *
from player import *
from level import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(nom_jeu)

clock = pygame.time.Clock()

level = Level(level_map, screen)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    screen.fill("black")
    level.draw_level()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
