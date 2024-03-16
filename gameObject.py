from pygame import Surface, Rect
import pygame


class GameObject:
    rect: Rect
    color: tuple[int, int, int] = (255, 255, 255)

    def __init__(self, rect: Rect) -> None:
        self.rect = rect

    def tick(self) -> None:
        pass

    def render(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
