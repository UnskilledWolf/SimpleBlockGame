from gameObject import GameObject


class Block(GameObject):
    color = (200, 200, 200)

    def collide(self):
        self.state.score += 1
        self.state.removeObject(self)
