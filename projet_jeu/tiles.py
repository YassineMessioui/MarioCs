import pygame
from images_importings import import_images


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, deplacement):
        self.rect.x += deplacement


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path, scale=1):
        super().__init__(size, x, y)
        self.frames = import_images(path)
        scaled_images = [
            pygame.transform.scale(
                image, (image.get_width() * scale, image.get_height() * scale)
            )
            for image in self.frames
        ]
        self.frames = scaled_images
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, deplacement):
        self.animate()
        self.rect.x += deplacement


class Coin(AnimatedTile):
    def __init__(self, size, x, y, path, val):
        super().__init__(size, x, y, path)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.val = val
