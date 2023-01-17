from abc import ABC
from enum import Enum


class Direction(Enum):
    north = 1
    south = 2
    west = 3
    east = 4
    north_west = 5
    north_east = 6
    south_west = 7
    south_east = 8


class Entity(ABC):
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self, direction: Direction):
        pass

