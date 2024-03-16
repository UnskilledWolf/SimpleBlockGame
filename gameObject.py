from pygame import Surface, Rect
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    print("Type Chekcing")
    from gameState import GameState


class GameObject:
    rect: Rect
    color: tuple[int, int, int] = (255, 255, 255)
    state: "GameState"

    def __init__(self, rect: Rect, state: "GameState") -> None:
        self.rect = rect
        self.state = state

    def tick(self) -> None:
        pass

    def render(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
