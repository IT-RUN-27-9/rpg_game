from src.incantation.incantation import Incantation


class Heal(Incantation):
    def cast(self, target):
        target.hp += 5
