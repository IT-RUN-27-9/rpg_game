from abc import ABC
from enum import Enum
from Player import Player
from src.fight.fight_realization import fight


class Direction(Enum):
    north = 1
    south = 2
    west = 3
    east = 4
    north_west = 5
    north_east = 6
    south_west = 7
    south_east = 8


def _check_borders(x_coord, y_coord):
    if x_coord > 100 or x_coord < 1 or y_coord < 1 or y_coord > 100:
        return False
    return True


class Entity(ABC):
    def __init__(self, x_coord, y_coord, hp, attack, game):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.hp = hp
        self.attack = attack
        self.game = game
        self.target = None
        self.in_battle = False

    def move(self, direction: Direction):
        new_x = None
        new_y = None
        if direction == Direction.east:
            new_x = self.x_coord + 1
            new_y = self.y_coord
        if direction == Direction.north:
            new_y = self.y_coord + 1
            new_x = self.x_coord
        if direction == Direction.west:
            new_x = self.x_coord - 1
            new_y = self.y_coord
        if direction == Direction.south:
            new_y = self.y_coord - 1
            new_x = self.x_coord
        if direction == Direction.north_west:
            new_x = self.x_coord - 1
            new_y = self.y_coord + 1
        if direction == Direction.north_east:
            new_x = self.x_coord + 1
            new_y = self.y_coord + 1
        if direction == Direction.south_east:
            new_x = self.x_coord + 1
            new_y = self.y_coord - 1
        if direction == Direction.south_west:
            new_x = self.x_coord - 1
            new_y = self.y_coord - 1
        if self._check(new_x, new_y):
            self.x_coord = new_x
            self.y_coord = new_y
            return True
        else:
            print('move is invalid')
            return False

    @staticmethod
    def _check_borders(x_coord, y_coord):
        if x_coord > 100 or x_coord < 1 or y_coord < 1 or y_coord > 100:
            return False
        return True

    def _check_other_objects(self, x_coord, y_coord):
        for monster in self.game.entities:
            if monster.x_coord == x_coord and monster.y_coord == y_coord:
                return False
            return True

    def _check(self, x_coord, y_coord):
        if self._check_borders(x_coord, y_coord) and self._check_other_objects(x_coord, y_coord):
            return True
        return False

    def set_target(self, target):
        self.target = target

    def _check_nearby(self, x_coord, y_coord):
        for monster in self.game.entities:
            if abs(monster.x_coord - x_coord) < 2 or abs(monster.y_coord - y_coord) < 2:
                fight(monster, Player)
            return False