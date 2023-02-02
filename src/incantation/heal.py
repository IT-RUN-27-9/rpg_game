from src.incantation.incantation import Incantation


class Heal(Incantation):
    def __init__(self):
        super().__init__(5, True, False)
    def cast(self, target):
        target.hp += 5
