from pygame import Surface
from pygame.event import Event
from gameObject import GameObject


class GameState:
    objects: list[GameObject] = []

    def events(self, event: Event) -> None:
        pass

    def render(self, screen: Surface) -> None:
        for o in self.objects:
            o.render(screen)

    def tick(self) -> None:
        pass
