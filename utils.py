import pygame


class ContaineredSprite(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


class PositionSprite(ContaineredSprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.position = pygame.Vector2(x, y)
