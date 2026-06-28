import pygame
import random


class Fish:
    def __init__(self):
        self.x = random.randint(0, 1280)
        self.y = random.randint(100, 650)

        self.speed = random.uniform(1, 3)
        self.direction = random.choice([-1, 1])

        self.size = random.randint(10, 18)

        # random vertical drift
        self.drift_timer = random.randint(30, 120)
        self.drift = 0

    def update(self):
        # horizontal movement
        self.x += self.speed * self.direction

        # small vertical “swim randomness”
        self.drift_timer -= 1
        if self.drift_timer <= 0:
            self.drift = random.uniform(-1, 1)
            self.drift_timer = random.randint(30, 120)

        self.y += self.drift

        # boundaries → flip direction
        if self.x < -20:
            self.x = 1280
        elif self.x > 1280:
            self.x = -20

        # keep fish inside vertical bounds
        if self.y < 80:
            self.y = 80
        elif self.y > 680:
            self.y = 680

    def draw(self, screen):
        # simple fish body (ellipse)
        color = (255, 180, 80)

        rect = pygame.Rect(self.x, self.y, self.size * 2, self.size)

        pygame.draw.ellipse(screen, color, rect)

        # eye
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (int(self.x + self.size), int(self.y + self.size / 3)),
            2
        )