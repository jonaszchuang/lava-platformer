import os
import pygame

class Start(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "start.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y