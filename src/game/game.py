import random

from src.entities.FileGolem import FireGolem
from src.entities.Monster import Monster
from src.entities.Player import Player
from src.entities.Rat import Rat
from src.entities.Vampire import Vampire
from src.entities.base_entity import Direction

def check_distance(monster, xcoord, ycoord):
    if ((monster.x_coord - xcoord)**2 + (monster.y_coord - ycoord)**2)**0.5 <= 2:
        return True

all_coords = []
set_all_coords = set()

def check_identical_coordinates(monsters):
    for monster in monsters:
        all_coords.append((monster.x_coord, monster.y_coord))
        set_all_coords.add((monster.x_coord, monster.y_coord))
    if len(all_coords) == len(list(set_all_coords)):
        return True


class Game:
    def __init__(self):
        self.entities = [Rat(random.randint(1, 100), random.randint(1, 100), self),
                         Rat(random.randint(1, 100), random.randint(1, 100), self),
                         Rat(random.randint(1, 100), random.randint(1, 100), self),
                         Monster(random.randint(1, 100), random.randint(1, 100), hp=10, attack=1, game=self),
                         FireGolem(random.randint(1, 100), random.randint(1, 100), self),
                         Vampire(random.randint(1, 100), random.randint(1, 100), self),
                         ]

        while check_identical_coordinates(self.entities) == False:
            self.entities = [Rat(random.randint(1, 100), random.randint(1, 100), self),
                             Rat(random.randint(1, 100), random.randint(1, 100), self),
                             Rat(random.randint(1, 100), random.randint(1, 100), self),
                             Monster(random.randint(1, 100), random.randint(1, 100), hp=10, attack=1, game=self),
                             FireGolem(random.randint(1, 100), random.randint(1, 100), self),
                             Vampire(random.randint(1, 100), random.randint(1, 100), self),
                             ]

        self.is_ended = False
        self.player = Player(random.randint(1, 100), random.randint(1, 100), self)

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
                for monster in self.entities:
                    monster.action()
            elif command == 2:
                self._move_player()
                for monster in self.entities:
                    monster.action()
            else:
                print('Неизвестная команда')
            return

    def show_info(self):
        print('Ничего не происходит')
        print(f'Ваши координаты: {self.player.x_coord}, {self.player.y_coord}')
        for monster in self.entities:
            if check_distance(monster, xcoord = self.player.x_coord, ycoord = self.player.y_coord):
                print(f"рядом с вами находится {monster}")