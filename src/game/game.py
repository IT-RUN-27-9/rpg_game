from src.entities.Player import Player
from src.entities.Rat import Rat
from src.entities.base_entity import  Direction


class Game:
    def __init__(self):
        self.entities = [Rat(5, 5, self), Rat(6, 6, self)]
        self.is_ended = False
        self.player = Player(1, 1, self)

    def _move_player(self):
        print("Вы")


    def get_command(self):
        while True:
            print('Выберите действие')
            print('1. Ничего не делать')
            print('2. Идти на север')

            command = int(input())
            if command == 1:
                pass
            elif command == 2:
                self.player.move(Direction.north)
            else:
                print('Неизвестная команда')
            return

    def show_info(self):
        print('Ничего не происходит')
        print(f'Ваши координаты: {self.player.x_coord}, {self.player.y_coord}')
