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
            direction = random.randint(1, 8)
            self.move(Direction(direction))
            print(f'коордитаны монстра: {self.get_coords()}')
