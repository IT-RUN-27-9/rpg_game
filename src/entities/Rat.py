from src.entities.Monster1 import Monster


class Rat(Monster):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord)
        self.attack = 2
        self.hp = 10