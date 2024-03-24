import pygame
from images_importings import import_images
from path import jump_folder_path, land_folder_path, explosion_folder_path


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == "jump":
            animation_images = import_images(jump_folder_path)
            scale = 1.5
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images
        if type == "land":
            animation_images = import_images(land_folder_path)
            scale = 1.5
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images
        if type == "explosion":
            animation_images = import_images(explosion_folder_path)
            scale = 1
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift
