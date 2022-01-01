import os
import pygame

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "fireball.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 64))

        self.rect.x = x
        self.rect.y = y

        self.move_speed = 3
        self.rect.width = 95
        self.rect.height = 60
