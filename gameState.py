from pygame import Surface, Rect
from pygame.event import Event
from ball import Ball
from block import Block
from gameObject import GameObject
from player import Player


class GameState:
    objects: list[GameObject] = []
    toRemove: list[GameObject] = []
    score: int = 0

    def __init__(self) -> None:
        self.addObject(Player(Rect(250, 350, 30, 10), self))
        self.addObject(Ball(Rect(250, 30, 5, 5), self))
        self.addObject(Block(Rect(240, 10, 20, 20), self))

    def events(self, event: Event) -> None:
        pass

    def render(self, screen: Surface) -> None:
        for o in self.objects:
            o.render(screen)

    def tick(self) -> None:
        for o in self.objects:
            o.tick()

        # Remove objects that are slated to be removed
        for o in self.toRemove:
            self.objects.remove(o)
        self.toRemove.clear()

    def addObject(self, o: GameObject) -> None:
        self.objects.append(o)

    def removeObject(self, o: GameObject) -> None:
        self.toRemove.append(o)
