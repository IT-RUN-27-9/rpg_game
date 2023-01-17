from src.entities.Monster1 import Monster
from src.incantation.incantation import Heal


class Mage(Monster):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord)
        self.mana = 20
        self.incantatoins = [Heal]

    def do_magic(self, target):
        target.hp -= self.incantatoins

