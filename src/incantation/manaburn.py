from src.incantation.incantation import Incantation


class Manaburn(Incantation):
    def cast(self, target):
        target.mana = 0