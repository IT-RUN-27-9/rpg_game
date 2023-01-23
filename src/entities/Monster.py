import random

from src.entities.base_entity import Entity, Direction


class Monster(Entity):
    def __init__(self, x_coord, y_coord, hp, attack, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.is_agro = True

    def hit(self, target):
        target.hp -= self.attack

    def get_coords(self):
        return self.x_coord, self.y_coord

    def _in_battle(self):
        return False

    def action(self):
        if self._in_battle():
            pass
        else:
            command = random.randint(1, 8)
            if command == 1:
                self.move(Direction.north)
            elif command == 2:
                self.move(Direction.south)
            elif command == 3:
                self.move(Direction.east)
            elif command == 4:
                self.move(Direction.west)
            elif command == 5:
                self.move(Direction.north_east)
            elif command == 6:
                self.move(Direction.north_west)
            elif command == 7:
                self.move(Direction.south_east)
            elif command == 8:
                self.move(Direction.south_west)
            print(f'коордитаны монстра: {self.get_coords()}')
