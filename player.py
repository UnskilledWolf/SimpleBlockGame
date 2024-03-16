from pygame import Rect
from gameObject import GameObject
import pygame


SPEED: float = 3


class Player(GameObject):
    color = (255, 255, 255)

    def __init__(self, rect: Rect) -> None:
        super().__init__(rect)

    def tick(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(SPEED, 0)
