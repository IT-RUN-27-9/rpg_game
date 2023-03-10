from src.entities.base_entity import Entity
import random


class Mage(Entity):
    def __init__(self, x_coord: int, y_coord: int, hp: int, attack: int, mana: int, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.mana = mana
        self.incantations = []

    def do_magic(self, target):
        self.incantations[0].cast(target)

