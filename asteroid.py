import os
import random

import pygame
from pygame.surface import Surface

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
from player import Player


PATH = os.path.join(os.path.dirname(__file__), "media", "asteroid", "asteroid_1.webp")
ASTEROID_IMAGE = pygame.image.load(PATH)


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.points_value = radius * 10

    def draw(self, screen: Surface):
        dr_image = pygame.transform.scale(
            ASTEROID_IMAGE, (self.radius * 2, self.radius * 2)
        )
        screen.blit(
            dr_image,
            (
                (self.position.x - ((self.radius * 2) / 2)),
                (self.position.y - ((self.radius * 2) / 2)),
            ),
        )

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
