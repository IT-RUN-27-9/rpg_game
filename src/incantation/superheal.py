from src.incantation.incantation import Incantation


class SuperHeal(Incantation):
    def cast(self, target):
        target.hp += 50