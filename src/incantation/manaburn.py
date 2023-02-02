from src.incantation.incantation import Incantation


class Manaburn(Incantation):
    def __init__(self):
        super().__init__(10)

    def cast(self, target):
        target.mana = 0