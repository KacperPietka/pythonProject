import pygame
from Player import Flappy
from Screen import Screen
from Obstacles import Rectangle


class Game:
    pygame.init()
    def __init__(self):
        self.run = True
        self.player = Flappy()
        self.screen = Screen(800, 600)
        self.rectangle = Rectangle()
        self.points = 0
        self.dead = False
        self.reward = 0
        self.background = (0,0,128)

    def restart(self):
        self.player.position = [10, 200]
        self.player.last_image_switch_time = 0
        self.player.speed = 0.05
        self.player.fall = 2
        self.points = 0
        Rectangle.rectangles = []
        Rectangle.last_image_switch_time = 0

    def points_adder(self):
        for rect in Rectangle.rectangles:
            if self.player.position[0] == rect.position[0] + rect.size[0] and rect.color == (0,123,0):
                self.points += 1
                self.reward = 10

    def collision(self):
        for rect in Rectangle.rectangles:
            if rect.color == self.background and (self.player.position[1] + self.player.height >= rect.position[1] + rect.size[1] or self.player.position[1] <= rect.position[1]) and (rect.position[0] <= self.player.position[0] + self.player.width <= (rect.position[0] + rect.size[0])):
                self.dead = True
                self.reward = -10
    def display_points(self):
        pygame.font.init()
        font = pygame.font.Font('arial.ttf', 50)
        text = font.render(f"{self.points}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(20, 30))
        self.screen.display.blit(text, text_rect)
        pygame.display.update()

    def play(self, move):
        clock = pygame.time.Clock()
        self.dead = False
        self.reward = 0
        self.screen.display.fill(self.background)
        self.rectangle.spawn_new_rec(self.screen.display)
        self.player.update_position(move)
        self.rectangle.update_position(self.screen.display)
        self.player.update_flappy_image()
        self.player.display_flappy_image(self.screen.display)
        self.collision()
        self.player.falling()
        self.points_adder()
        self.display_points()

        # Check if player hits boundaries
        if self.player.position[1] >= self.screen.height - self.player.height or self.player.position[1] <= 0:
            self.dead = True
            self.reward = -10

        # Update Pygame display
        pygame.display.update()

        # Process events (e.g., quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(60)

        return self.reward, self.dead, self.points
