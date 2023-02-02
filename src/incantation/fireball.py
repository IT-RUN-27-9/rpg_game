from src.incantation.incantation import Incantation


class Fireball(Incantation):
    def __init__(self):
        super().__init__(12, False, True)
    def __str__(self):
        return 'Огненный шар'

    def cast(self, target):
        target.hp -= 15
