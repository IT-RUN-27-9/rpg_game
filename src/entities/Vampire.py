from src.entities.Mage import Mage
from src.entities.Monster import Monster
from src.incantation.fireball import Fireball


class Vampire(Mage, Monster):
    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 100, 3, 25, game)
        self.incantations = [Fireball()]

    def __str__(self):
        return "Вампир"
