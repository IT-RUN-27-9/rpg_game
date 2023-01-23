from src.entities.Player import Player
from src.entities.Rat import Rat
from src.entities.base_entity import Direction
from src.entities.base_entity import Entity
import random
from random import randint

def check_distance(monster, xcoord, ycoord):
    if ((monster.x_coord - xcoord)**2 + (monster.y_coord - ycoord)**2)**0.5 <= 2:
        return True


class Game:
    def __init__(self):
        self.entities = [Rat(5, 5, self), Rat(6, 6, self)]
        self.is_ended = False
        self.player = Player(1, 1, self)

    def randomly_move_monsters(self):
        for monster in self.entities:
            new_x = monster.x_coord + randint(-1, 1)
            new_y = monster.y_coord + randint(-1, 1)
            if monster._check(new_x, new_y):
                monster.x_coord = new_x
                monster.y_coord = new_y

    def _move_player(self):
        print("""Выберите направление:
        1.Север
        2.Юг
        3.Восток
        4.Запад
        5.Северо-восток
        6.Северо-запад
        7.Юго-восток
        8.Юго-запад""")
        command = int(input())
        if command == 1:
            self.player.move(Direction.north)
        elif command == 2:
            self.player.move(Direction.south)
        elif command == 3:
            self.player.move(Direction.east)
        elif command == 4:
            self.player.move(Direction.west)
        elif command == 5:
            self.player.move(Direction.north_east)
        elif command == 6:
            self.player.move(Direction.north_west)
        elif command == 7:
            self.player.move(Direction.south_east)
        elif command == 8:
            self.player.move(Direction.south_west)


    def get_command(self):
        while True:
            print('Выберите действие')
            print('1. Ничего не делать')
            print('2. Сделать ход')

            command = int(input())
            if command == 1:
                pass
            elif command == 2:
                self._move_player()
                self.randomly_move_monsters()
            else:
                print('Неизвестная команда')
            return

    def show_info(self):
        print('Ничего не происходит')
        print(f'Ваши координаты: {self.player.x_coord}, {self.player.y_coord}')
        for monster in self.entities:
            if check_distance(monster, xcoord = self.player.x_coord, ycoord = self.player.y_coord):
                print(f"рядом с вами находится {monster}")

