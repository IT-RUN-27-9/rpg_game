from src.entities.Mage import Mage
from src.incantation.fireball import Fireball
from src.incantation.superheal import SuperHeal


class Player(Mage):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord)
        self.hp = 100
        self.attack = 10
        self.mana = 50
        self.incantatoins = [SuperHeal, Fireball]
