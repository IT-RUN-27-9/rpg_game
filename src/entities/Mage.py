from src.entities.base_entity import Entity, Direction
from src.incantation.heal import Heal
import random


class Mage(Entity):
    def __init__(self, x_coord: int, y_coord: int, hp: int, attack: int, mana: int, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.mana = mana
        self.incantations = [Heal()]

    def do_magic(self, target):
        target.hp -= self.incantations

    def get_coords(self):
        return self.x_coord, self.y_coord

    def action_mage(self):
        if self.in_battle:
            miss_chance_25 = random.randint(1, 4)
            if miss_chance_25 != 4:
                self.do_magic(self.target)
        else:
            direction = random.randint(1, 8)
            self.move(Direction(direction))
            print(f'координаты монстра: {self.get_coords()}')
