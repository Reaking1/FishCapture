import pygame
import random
from fish import Fish
from dolphin import Dolphin



class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.uniform(0.5, 2)
        self.size = random.randint(2, 5)

    def update(self):
        self.y -= self.speed

        if self.y < 0:
            self.y = 720
            self.x = random.randint(0, 1280)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 230, 255),
            (int(self.x), int(self.y)),
            self.size
        )


class World:
    def __init__(self):
        self.background = pygame.image.load(
            "assets/backgrounds/background_terrain.png"
        )
        self.background = pygame.transform.scale(self.background, (1280, 720))

        self.bubbles = [
            Bubble(random.randint(0, 1280), random.randint(0, 720))
            for _ in range(60)
        ]

        self.fishes = [Fish() for _ in range(8)]

        self.dolphin = Dolphin()

        self.time = 0

    def update(self):
        self.time += 1

        for bubble in self.bubbles:
            bubble.update()

        for fish in self.fishes[:]:
            fish.update()

            dx = self.dolphin.x - fish.x
            dy = self.dolphin.y - fish.y
            distance = (dx * dx + dy * dy) ** 0.5

            if distance < 40:
                self.fishes.remove(fish)

        self.dolphin.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for bubble in self.bubbles:
            bubble.draw(screen)

        for fish in self.fishes:
            fish.draw(screen)

        self.dolphin.draw(screen)
    def __init__(self):
        self.background = pygame.image.load("assets/backgrounds/background_terrain.png")
        self.background = pygame.transform.scale(self.background, (1280, 720))

        self.bubbles = []
        for _ in range(60):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            self.bubbles.append(Bubble(x, y))

        self.fishes = []
        for _ in range(8):
            self.fishes.append(Fish())

        self.dolphin = Dolphin()
        self.time = 0

    def update(self):
        self.time += 1

        for bubble in self.bubbles:
            bubble.update()

        for fish in self.fishes[:]:
            fish.update()

            dx = self.dolphin.x - fish.x
            dy = self.dolphin.y - fish.y
            distance = (dx * dx + dy * dy) ** 0.5

            if distance < 40:
                self.fishes.remove(fish)

        self.dolphin.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for bubble in self.bubbles:
            bubble.draw(screen)

        for fish in self.fishes:
            fish.draw(screen)

        self.dolphin.draw(screen)
    def __init__(self):
        # background image
        self.background = pygame.image.load("assets/backgrounds/background_terrain.png")
        self.background = pygame.transform.scale(self.background, (1280, 720))

        # bubbles
        self.bubbles = []
        for _ in range(60):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            self.bubbles.append(Bubble(x, y))

        # fish
        self.fishes = []
        for _ in range(8):
            self.fishes.append(Fish())

        # dolphin
        self.dolphin = Dolphin()

        self.time = 0

    def update(self):
        self.time += 1

        for bubble in self.bubbles:
            bubble.update()

        for fish in self.fishes[:]:
            fish.update()

            dx = self.dolphin.x - fish.x
            dy = self.dolphin.y - fish.y
            distance = (dx * dx + dy * dy) ** 0.5

    if distance < 40:
        self.fishes.remove(fish)

        self.dolphin.update()

    def draw(self, screen):
        # background
        screen.blit(self.background, (0, 0))

        # bubbles
        for bubble in self.bubbles:
            bubble.draw(screen)

        # fish
        for fish in self.fishes:
            fish.draw(screen)

        # dolphin on top
        self.dolphin.draw(screen)