import os
import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "heart.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))


        self.rect.x = x
        self.rect.y = y
