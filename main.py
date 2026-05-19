import sys
import pygame

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from shot import Shot


def main() -> None:
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        clock = pygame.time.Clock()

        log_state()

        screen.fill("black")

        updatable.update(dt)
        collision = any(player.collides_with(asteroid) for asteroid in asteroids)
        if collision:
            log_event("player_hit")
            print("Game Over!")
            sys.exit()

        [
            shot.collides_with(asteroid) and asteroid.kill()
            for asteroid in asteroids
            for shot in shots
        ]

        [item.draw(screen) for item in drawable]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
