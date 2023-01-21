from src.entities.Mage import Mage
from src.incantation.fireball import Fireball


class FireGolem(Mage):
    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 100, 50, 25, game)
        self.incantations = [Fireball]
