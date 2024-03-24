from csv import reader
from settings import tile_size
import pygame


def import_csv_layout(chemin):
    terrain_map = []
    with open(chemin) as file:
        level = reader(file, delimiter=",")
        for row in level:
            terrain_map.append(list(row))
        return terrain_map


def import_cut_graphics(chemin):
    surface = pygame.image.load(chemin).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)
    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surf)

    return cut_tiles
