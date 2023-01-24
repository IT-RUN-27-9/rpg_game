from src.entities.Monster import Monster
from src.incantation.heal import Heal


class Mage(Monster):
    def __init__(self, x_coord, y_coord, hp, attack, mana, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.mana = mana + 3
        self.incantations = [Heal]

    def do_magic(self, target):
        target.hp -= self.incantations

