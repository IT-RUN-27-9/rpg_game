from src.incantation.incantation import Incantation


class SuperHeal(Incantation):
    def __init__(self):
        super().__init__(15, True, False)
    def __str__(self):
        return 'Super heal'
    def cast(self, target):
        target.hp += 50
