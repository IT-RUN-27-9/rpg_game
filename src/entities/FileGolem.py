from src.entities.Mage import Mage
from src.incantation.fireball import Fireball


class FireGolem(Mage):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord, 100, 50, 25)
        self.incantations = [Fireball]
