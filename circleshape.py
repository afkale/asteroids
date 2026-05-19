from typing import Self
import pygame

from utils import PositionSprite


class CircleShape(PositionSprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y)

        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen): ...

    def update(self, dt): ...

    def collides_with(self, other: Self):
        distance = self.position.distance_to(other.position)
        radius = self.radius + other.radius
        return radius > distance
