import pygame


class Rectangle:
    def __init__(self):
        self.position = [750, 250]
        self.size = [60, 800]
        self.last_image_switch_time = 0

    def spawn_rec(self):
        self.position = [750, 250]

    def draw_obstacles(self, screen):
        pygame.draw.rect(screen, (0, 123, 0),
                         pygame.Rect(self.position[0], self.position[1], self.size[0],
                                     self.size[1]))

    def spawn_rec(self, screen):
        new_rec = UpperRec()
        new_rec.position = [750, 0]
        current_time = pygame.time.get_ticks()
        if current_time - new_rec.last_image_switch_time >= 3000:
            new_rec.last_image_switch_time = current_time
            pygame.draw.rect(screen, (0, 123, 0),
                             pygame.Rect(new_rec.position[0], new_rec.position[1], new_rec.size[0],
                                         new_rec.size[1]))
    def update_position(self):
        self.position[0] -= 2
class LowerRec(Rectangle):
    def __init__(self):
        super().__init__()
        self.position = [750, 250]
        self.size = [60, 800]
        self.last_image_switch_time = 0

    def spawn_rec(self):
        super().spawn_rec()
        self.position = [750, 250]

class UpperRec(Rectangle):
    def __init__(self):
        super().__init__()
        self.position = [750, 0]
        self.size = [60, 100]
        self.last_image_switch_time = 0
    def spawn_rec(self):
        super().spawn_rec()
        self.position = [750, 0]
