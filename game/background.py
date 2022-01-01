import os
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "background.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()


        self.rect.x = 0
        self.rect.y = 0
