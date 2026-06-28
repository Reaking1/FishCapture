import pygame

class Dolphin:
    def __init__(self):
        self.x = 640
        self.y = 360
        self.speed = 5
        self.size = 30

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # smooth follow
        self.x += (mouse_x - self.x) * 0.1
        self.y += (mouse_y - self.y) * 0.1

    def draw(self, screen):
        pygame.draw.ellipse(
            screen,
            (80, 200, 255),
            (self.x - 30, self.y - 15, 60, 30)
        )