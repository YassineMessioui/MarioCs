from pygame.locals import *
from pygame import mixer


def music(path, volume):
    sound = mixer.Sound(path)
    sound.set_volume(volume)
    sound.play()
