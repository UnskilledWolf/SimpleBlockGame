from pygame import Surface


class GameObject:
    x: float = 0
    y: float = 0

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def render(self, screen: Surface) -> None:
        pass
