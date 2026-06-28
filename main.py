import pygame
import sys
from world import World

# Initialize pygame
pygame.init()

# Window settings
WIDTH = 1280
HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐬 Dolphin Fish Capture")

clock = pygame.time.Clock()

world = World()

running = True

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background color (ocean blue)
    world.update()
    world.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()