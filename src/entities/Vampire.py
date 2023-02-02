from src.entities.Mage import Mage
from src.entities.Monster import Monster
from src.incantation.fireball import Fireball
from src.incantation.manaburn import Manaburn


class Vampire(Mage, Monster):
    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 150, 15, 10, game)
        self.incantations = [Fireball(), Manaburn()]

    def __str__(self):
        return "Вампир"
