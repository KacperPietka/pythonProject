import pygame
from Player import Flappy
from Screen import Screen
from Obstacles import UpperRec
from Obstacles import LowerRec

class Game:
    def __init__(self):
        self.run = True
        self.player = Flappy()
        self.screen = Screen(800, 533)
        self.upperRec = UpperRec()
        self.lowerRec = LowerRec()
        self.last_image_switch_time = 0  # Track time for image switching
        self.image_index = 0

    def game_over(self):
        font = pygame.font.Font('arial.ttf', 32)
        text = font.render('YOU LOST!', True, (0, 0, 0))
        text_rect = text.get_rect()
        self.screen.display.fill((0,0,0))

    def update_flappy_image(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_image_switch_time >= 300:
            self.last_image_switch_time = current_time
            self.image_index = (self.image_index + 1) % 3

    def display_flappy_image(self):
        if self.image_index == 0:
            self.player.display_image_1(self.screen.display)
        elif self.image_index == 1:
            self.player.display_image_2(self.screen.display)
        elif self.image_index == 2:
            self.player.display_image_3(self.screen.display)

    def update_obstacles_position(self):
        self.upperRec.position[0] -= 2
        self.lowerRec.position[0] -= 2
    def draw_obstacles(self):
        pygame.draw.rect(self.screen.display, (0, 123, 0),
                         pygame.Rect(self.upperRec.position[0], self.upperRec.position[1], self.upperRec.size[0],
                                     self.upperRec.size[1]))
        pygame.draw.rect(self.screen.display, (0, 123, 0),
                         pygame.Rect(self.lowerRec.position[0], self.lowerRec.position[1], self.lowerRec.size[0],
                                     self.lowerRec.size[1]))
    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            time_counter = clock.tick()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            key = pygame.key.get_pressed()
            self.player.update_position(key)
            self.player.position[1] += 1
            self.update_obstacles_position()
            if self.player.position[1] >= self.screen.height - self.player.height or self.player.position[1] <= 0:
                #self.game_over()
                run = False
            self.screen.display.fill((0, 0, 128))
            self.draw_obstacles()

            self.update_flappy_image()
            self.display_flappy_image()

            pygame.display.update()
        pygame.quit()