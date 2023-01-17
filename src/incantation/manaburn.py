from src.incantation.incantation import Incantation


class Fireball(Incantation):
    def cast(self, target):
        target.mana = 0