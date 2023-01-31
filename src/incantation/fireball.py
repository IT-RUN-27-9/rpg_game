from src.incantation.incantation import Incantation


class Fireball(Incantation):
    def __str__(self):
        return 'Огненный шар'

    def cast(self, target):
        target.hp -= 70
