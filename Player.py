import pygame
from Screen import Screen


class Shiba:
    def __init__(self):
        self.image = pygame.image.load('shiba_sprite.png')
        self.position = [10, 200]
        self.height = 84
        self.width = 114
    def update_position(self, key):
        if key[pygame.K_SPACE]:
            self.position[1] -= 10
    def display(self, screen):
        screen.blit(self.image, (self.position[0], self.position[1]))