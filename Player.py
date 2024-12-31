import pygame
from Screen import Screen


class Flappy:
    def __init__(self):
        self.image1 = pygame.image.load('flappy.png')
        self.image2 = pygame.image.load('flappy2.png')
        self.image3 = pygame.image.load('flappy3.png')
        self.position = [10, 200]
        self.height = 84
        self.width = 114
    def update_position(self, key):
        if key[pygame.K_SPACE]:
            self.position[1] -= 10
    def display_image_1(self, screen):
        screen.blit(self.image1, (self.position[0], self.position[1]))
    def display_image_2(self, screen):
        screen.blit(self.image2, (self.position[0], self.position[1]))
    def display_image_3(self, screen):
        screen.blit(self.image3, (self.position[0], self.position[1]))
