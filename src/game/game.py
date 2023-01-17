from src.entities.base_entity import Entity


class Player(Entity):
    pass

class Game:
    def __init__(self):
        self.entites = []
        self.is_ended = False
        self.player = Player

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


