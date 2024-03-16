from pygame import Rect, Surface, Vector2
import pygame
from block import Block
from gameObject import GameObject
from typing import TYPE_CHECKING
from player import Player

if TYPE_CHECKING:
    print("Type Chekcing")
    from gameState import GameState


class Ball(GameObject):
    color = (255, 255, 255)
    velocity: Vector2

    def __init__(self, pos: Vector2, state: "GameState") -> None:
        super().__init__(Rect(pos.x, pos.y, 10, 10), state)
        self.velocity = Vector2(2.5, 5)

    def tick(self) -> None:
        self.rect.move_ip(self.velocity)

        for o in self.state.objects:
            if type(o) == Block:
                if self.rect.colliderect(o.rect):
                    o.collide()
                    self.deflect()
            elif type(o) == Player:
                if self.rect.colliderect(o.rect):
                    self.deflect()

        if self.rect.top < 0:
            self.deflect()
        elif self.rect.left < 0 or self.rect.right > 500:
            self.deflect(True, False)
        elif self.rect.bottom > 400:
            self.state.gameOver()

    def deflect(self, x: bool = False, y: bool = True) -> None:
        if x:
            self.velocity.x *= -1

        if y:
            self.velocity.y *= -1

    def render(self, screen: Surface) -> None:
        pygame.draw.circle(screen, self.color, self.rect.center, 5)
        # pygame.draw.rect(screen, (0, 255, 0), self.rect)
