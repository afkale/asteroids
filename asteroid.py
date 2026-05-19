import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from player import Player


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.points_value = radius * 10

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def kill(self, player: Player) -> None:
        log_event("asteroid_shot")

        super().kill()
        player.points += self.points_value
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        self.split()

    def split(self) -> None:
        log_event("asteroid_split")
        angle = random.uniform(ASTEROID_MIN_RADIUS, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_a.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_b.velocity = self.velocity.rotate(-angle) * 1.2
