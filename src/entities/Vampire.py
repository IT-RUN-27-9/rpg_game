from src.entities.Mage import Mage


class Vampire(Mage):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord, 100, 3, 25)
        self.incantations = []