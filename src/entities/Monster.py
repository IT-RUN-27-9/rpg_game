import random

from src.entities.Mage import Mage
from src.entities.base_entity import Entity, Direction


class Monster(Entity):
    def __init__(self, x_coord: int, y_coord: int, hp: int, attack: int, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.in_battle = False

    def hit(self, target):
        target.hp -= self.attack

    def get_coords(self):
        return self.x_coord, self.y_coord

    def action(self):
        if self.in_battle:
            self.hit(self.target)
        else:
            direction = random.randint(1, 8)
            self.move(Direction(direction))
            print(f'координаты монстра: {self.get_coords()}')
