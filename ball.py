from pygame import Surface, Vector2
import pygame
from block import Block
from gameObject import GameObject
from player import Player


class Ball(GameObject):
    color = (255, 255, 255)
    velocity: Vector2 = Vector2(2.5, 5)

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
            self.velocity.x *= -1
        elif self.rect.bottom > 400:
            self.deflect()

    def deflect(self) -> None:
        print("Ball deflecting")

        self.velocity.y *= -1

    def render(self, screen: Surface) -> None:
        pygame.draw.circle(screen, self.color, self.rect.center, 5)
