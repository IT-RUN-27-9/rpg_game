from src.entities.Mage import Mage
from src.incantation.fireball import Fireball
from src.incantation.superheal import SuperHeal


class Player(Mage):

    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 500, 50, 25, game)
        self.incantations = [SuperHeal(), Fireball()]

    def do_magic(self, target):
        i = 0
        print('Выберите заклинание')
        for incantation in self.incantations:
            i += 1
            print(f'{i}. {incantation}')
        command = int(input())
        if target is None:
            print("Выберите цель")
        incantation = self.incantations[command - 1]
        incantation.cast(target)
        self.mana -= incantation.mana
