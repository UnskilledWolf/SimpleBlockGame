from pygame import Surface, Rect, Vector2
import pygame
from pygame.event import Event
from ball import Ball
from block import Block
from gameObject import GameObject
from player import Player
from pygame.font import Font


class GameState:
    objects: list[GameObject]
    toRemove: list[GameObject]
    font: Font
    score: int
    winScore: int
    paused: bool
    canUnpause: bool

    def __init__(self, font: Font) -> None:
        self.font = font

        self.objects = []
        self.toRemove = []

        self.initializeGame()

    def events(self, event: Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and self.canUnpause:
                self.paused = not self.paused
            elif event.key == pygame.K_r:
                self.initializeGame()

    def render(self, screen: Surface) -> None:
        for o in self.objects:
            o.render(screen)

        if self.paused:
            text = "Paused"

            if not self.canUnpause:
                if self.score >= self.winScore:
                    text = "Win!"
                else:
                    text = "Game Over!"

            img = self.font.render(text, True, (255, 0, 0))
            pos = Vector2(250 - img.get_width() / 2, 200 - img.get_height() / 2)
            screen.blit(img, pos)

    def tick(self) -> None:
        if self.paused:
            return

        for o in self.objects:
            o.tick()

        # Remove objects that are slated to be removed
        for o in self.toRemove:
            self.objects.remove(o)
        self.toRemove.clear()

        if self.score >= self.winScore:
            self.gameOver()

    def addObject(self, o: GameObject) -> None:
        self.objects.append(o)

    def removeObject(self, o: GameObject) -> None:
        self.toRemove.append(o)

    def initializeGame(self) -> None:
        self.objects.clear()
        self.toRemove.clear()

        self.score = 0
        self.winScore = 0
        self.paused = False
        self.canUnpause = True

        self.addObject(Player(Rect(250, 350, 50, 5), self))
        self.addObject(Ball(Vector2(250, 300), self))

        # Place Blocks
        cols: int = 10
        rows: int = 5

        self.winScore = rows * cols

        for r in range(rows):
            for c in range(cols):
                self.addObject(Block(Rect(5 + c * 55, 5 + r * 25, 50, 20), self))

    def gameOver(self) -> None:
        self.paused = True
        self.canUnpause = False
