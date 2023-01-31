from src.entities.base_entity import Entity, Direction
from src.incantation.heal import Heal
import random


class Mage(Entity):
    def __init__(self, x_coord: int, y_coord: int, hp: int, attack: int, mana: int, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.mana = mana
        self.incantations = []

    def do_magic(self, target):
        self.incantations[0].cast(target)

    def action_in_battle(self):
        miss_chance_25 = random.randint(1, 4)
        if miss_chance_25 != 4:
            self.do_magic(self.target)
