from base_entity import Entity
from src.incantation.incantation import Heal, Fireball


class Monster(Entity):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord, 20, 3)
        self.is_agro = True

    def hit(self, target):
        target.hp -= self.attack
