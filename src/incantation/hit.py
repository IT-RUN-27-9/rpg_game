from src.incantation.incantation import Incantation


class Hit(Incantation):
    def __str__(self):
        return 'Ударить'

    def cast(self, target):
        target.hp -= 10