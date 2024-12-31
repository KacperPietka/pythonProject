import pygame
from Player import Shiba
from Screen import Screen
from Obstacles import UpperRec
from Obstacles import LowerRec

class Game:
    def __init__(self):
        self.run = True
        self.player = Shiba()
        self.screen = Screen(800, 533)
        self.upperRec = UpperRec()
        self.lowerRec = LowerRec()

    def game_over(self):
        font = pygame.font.Font('arial.ttf', 32)
        text = font.render('YOU LOST!', True, (0, 0, 0))
        text_rect = text.get_rect()
        self.screen.display.fill((0,0,0))

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            key = pygame.key.get_pressed()
            pygame.draw.rect(self.screen.display, (0, 123, 0), pygame.Rect(30, 30, 60, 60), 2)
            self.player.update_position(key)
            self.player.position[1] += 1
            self.upperRec.position[0] -= 2
            self.lowerRec.position[0] -= 2
            if self.player.position[1] >= self.screen.height - self.player.height or self.player.position[1] <= 0:
                #self.game_over()
                run = False
            self.screen.display.fill((0, 0, 128))
            pygame.draw.rect(self.screen.display, (0, 123, 0),
                             pygame.Rect(self.upperRec.position[0], self.upperRec.position[1], self.upperRec.size[0],
                                         self.upperRec.size[1]))
            pygame.draw.rect(self.screen.display, (0, 123, 0),
                             pygame.Rect(self.lowerRec.position[0], self.lowerRec.position[1], self.lowerRec.size[0],
                                         self.lowerRec.size[1]))
            self.player.display(self.screen.display)

            pygame.display.update()
        pygame.quit()