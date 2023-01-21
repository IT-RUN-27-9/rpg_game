from src.entities.base_entity import Entity


class Monster(Entity):
    def __init__(self, x_coord, y_coord, hp, attack, game):
        super().__init__(x_coord, y_coord, hp, attack, game)
        self.is_agro = True

    def hit(self, target):
        target.hp -= self.attack
