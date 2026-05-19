import pygame
from pygame.surface import Surface

from player import Player
from utils import PositionSprite


class TextSprite(PositionSprite):
    def __init__(
        self,
        x: int,
        y: int,
        font_size: int = 36,
        font_family: str | None = None,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        super().__init__(x, y)
        self.color = color
        self.font_size = font_size
        self.font_family = font_family
        self.font = pygame.font.Font(font_family, font_size)


class PointsCounter(TextSprite):
    def __init__(
        self,
        player: Player,
        x: int = 2,
        y: int = 2,
        font_size: int = 36,
        font_family: str | None = None,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        super().__init__(x, y, font_size, font_family, color)
        self.__player = player

    def draw(self, screen: Surface):
        text = self.font.render(f"Points: {self.__player.points}", True, self.color)
        screen.blit(text, self.position)
