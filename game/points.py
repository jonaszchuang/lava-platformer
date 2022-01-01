import os
import pygame

class Points(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "points.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))


        self.rect.x = x
        self.rect.y = y

        self.rect.width = 50
        self.rect.height = 50
