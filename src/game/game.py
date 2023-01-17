from random import randrange
from src.entities.base_entity import Entity


class Player(Entity):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord)
        self.hp = 500
        self.x_coord = randrange(100)
        self.y_coord = randrange(100)

class Game:
    def __init__(self):
        self.entites = []
        self.is_ended = False
        self.player = Player(self)

    def get_command(self):
        while True:
            print('Выберите действие')
            print('1. Ничего не делать')
            command = int(input())
            if command != 1:
                print('Неизвестная команда')
            return


    def show_info(self):
        print('Ничего не происходит')


