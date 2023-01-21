from src.entities.Mage import Mage
from src.incantation.fireball import Fireball
from src.incantation.superheal import SuperHeal


class Player(Mage):
    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 500, 50, 25, game)
        self.incantatoins = [SuperHeal, Fireball]
