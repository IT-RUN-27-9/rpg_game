from src.entities.Mage import Mage
from src.incantation.fireball import Fireball
from src.incantation.superheal import SuperHeal
from src.game.game import Game


class Player(Mage):

    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 500, 50, 25, game)
        self.incantatoins = [SuperHeal(), Fireball()]

    def do_magic(self, target):
        i = 0
        print('Выберите заклинание')
        for incantation in self.incantatoins:
            i += 1
            print(f'{1}. {incantation}')
        command = int(input())
        self.incantatoins[command - 1].cast(target)
