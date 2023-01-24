from src.entities.Mage import Mage
from src.entities.Monster import Monster


class Vampire(Mage, Monster):
    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 100, 3, 25, game)
        self.incantations = []