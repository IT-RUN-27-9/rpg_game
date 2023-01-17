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

    def move(self, direction: Direction, ):
        if self._check(x_coord, y_coord):
            if direction == Direction.east:
                self.x_coord += 1
            if direction == Direction.north:
                self.y_coord += 1
            if direction == Direction.west:
                self.x_coord -= 1
            if direction == Direction.south:
                self.y_coord -= 1
            return True
        else:
            print('move is invalid')
            return False

    def _check_borders(self, x_coord, y_coord):
        if x_coord > 100 or x_coord < 1 or y_coord < 1 or y_coord > 100:
            return False
        return True

    def _check_other_objects(self, x_coord, y_coord):
        for monster in monsters:
            if monster.x_coord == x_coord and monster.y_coord == y_coord:
                return False
            return True

    def _check(self, x_coord, y_coord):
        if self._check_borders(x_coord, y_coord) and self._check_other_objects(x_coord, y_coord):
            return True
        return False



# Дописать метод move для базового класса существ.
# Метод должен принимать елемент enum Direction и объект класса game.
# Нужно сделать проверки что на целевой точке не стоит другое существо
# (перебрать всех существ из игры) и проверить что она находится в допустимом диапазоне.
# После этого если все ок, то сдвинуть существо и вернуть True,
# иначе вывести на консоль сообщение об ошибке и вернуть False.
