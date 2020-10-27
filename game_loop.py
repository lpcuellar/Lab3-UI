import pygame

from math import cos, sin, pi

textures = {
    '1' : pygame.image.load('./textures/stone_iron_wall.png'),
    '2' : pygame.image.load('./textures/stone_torch.png'),
    '3' : pygame.image.load('./textures/iron_x.png'),
    '4' : pygame.image.load('./textures/iron_wall.png'),
}

class Game():
    def __init__(self):
        pygame.init()