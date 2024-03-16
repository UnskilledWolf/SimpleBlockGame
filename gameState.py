from pygame import Surface, Rect
from pygame.event import Event
from gameObject import GameObject
from player import Player


class GameState:
    objects: list[GameObject] = []

    def __init__(self) -> None:
        self.addObject(Player(Rect(250, 350, 30, 10)))

    def events(self, event: Event) -> None:
        pass

    def render(self, screen: Surface) -> None:
        for o in self.objects:
            o.render(screen)

    def tick(self) -> None:
        for o in self.objects:
            o.tick()

    def addObject(self, o: GameObject) -> None:
        self.objects.append(o)
