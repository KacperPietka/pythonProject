import pygame
class Flappy:
    def __init__(self):
        self.image1 = pygame.image.load('flappy.png')
        self.image2 = pygame.image.load('flappy2.png')
        self.image3 = pygame.image.load('flappy3.png')
        self.position = [10, 200]
        self.height = 37
        self.width = 50
        self.image_index = 0
        self.last_image_switch_time = 0
    def update_position(self, key):
        if key[pygame.K_SPACE]:
            self.position[1] -= 10

    def falling(self):
        self.position[1] += 1
    def update_flappy_image(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_switch_time >= 300:
            self.last_image_switch_time = current_time
            self.image_index = (self.image_index + 1) % 3

    def display_flappy_image(self, screen):
        if self.image_index == 0:
            screen.blit(self.image1, (self.position[0], self.position[1]))
        elif self.image_index == 1:
            screen.blit(self.image2, (self.position[0], self.position[1]))
        elif self.image_index == 2:
            screen.blit(self.image3, (self.position[0], self.position[1]))

